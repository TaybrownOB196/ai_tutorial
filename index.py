from flask import Flask, render_template, jsonify, request
import csv
import os
from dotenv import load_dotenv
import joblib

load_dotenv()

app = Flask(__name__)
loaded_model = joblib.load('ttt.model')

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/tictactoe', methods=['GET'])
def get():
    player=request.args['player']
    return render_template('tictactoe.html', player=player)

@app.route('/tictactoe', methods=['POST'])
def post():
    #record board data for csv file
    data = request.get_json()
    error_response = jsonify({'error': 'invalid payload'})
    if not data:
        return error_response, 400
        
    board = data.get('board')
    label = data.get('label')
    if not board or not label:
        return error_response, 400
    
    result_set = [*board, label]
    write_result_set(result_set)
    return jsonify({}), 200

@app.route('/tictactoe/nextmove', methods=['POST'])
def get_next_move():
    data = request.get_json()
    board = data.get('board')
    res = loaded_model.predict([board]).tolist()[0]
    payload = {
        "move": res
    }
    print(payload)
    return jsonify(payload), 200

def write_result_set(result_set):
    with open(os.getenv('T3_DATA_FILE_PATH'), 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(result_set)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=8080)