from flask import Flask, render_template, jsonify, request
import csv
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

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

def write_result_set(result_set):
    with open(os.getenv("T3_DATA_FILE_PATH"), 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(result_set)

