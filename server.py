from flask import Flask, jsonify, render_template, request
from MLModel import modelOutput, visualizationData

app = Flask(__name__)

@app.route('/_model_output')
def model_output():
	return jsonify(result=modelOutput())

@app.route('/_model_data')
def model_data():
	return jsonify(result=visualizationData())

@app.route('/')
def index():
	return render_template('index.html')


