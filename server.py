from flask import Flask, request, jsonify, url_for, redirect, render_template
import json
app = Flask(__name__)

@app.route('/words', methods = ['POST'])
def words():
	if request.is_json:
		words_input = request.get_json()
		# return jsonify({words_input: request['words_input']})
		# print (words_input['words_input'])
		if words_input != "":
			return '{"words_input": "input sccessful"}'
		else:
			return '{"words_input": "no input"}'
		
	return '{"error": "expecting json"}'

@app.route('/palindrome/')
def palindrome():
	return render_template('Palindrome_Algorithm_02.js')

@app.route('/')
def basic():
	return render_template('index.html')