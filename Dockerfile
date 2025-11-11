FROM python:3.13.9

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "index.py" ]