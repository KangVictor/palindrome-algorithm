from flask import Flask, request, jsonify, url_for, redirect, render_template
import json
app = Flask(__name__)

@app.route('/words', methods = ['POST'])
def words():
	if request.is_json:
		words_input = request.get_json()
		return '{"words_input": "input sccessful"}'
	return '{"error": "expecting json"}'

@app.route('/')
def basic():
	return render_template('index.html')