import flask
import psycopg2
from flask import request, jsonify

app = flask.Flask(__name__)


@app.route("/")
def hello():
	db = psycopg2.connect("host=db dbname=postgres user=flask_user password=qwerty")
	return "OK"
	

if __name__ == "__main__":
	app.run(host='0.0.0.0')