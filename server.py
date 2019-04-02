from flask import Flask, request, jsonify, url_for, redirect, render_template
import json
app = Flask(__name__)

@app.route('/words', methods = ['POST'])
def words():
	if request.is_json:
		getWord = request.get_json()
		print (getWord['words_input'])
		# write words_input on words_data.txt
		f = open("words_data.txt","a+")
		f.write("\n%s" % getWord['words_input'])
		f.close()
	return 'true'

@app.route('/palindrome/')
def palindrome():
	return render_template('Palindrome_Algorithm_02.js')

@app.route('/')
def basic():
	return render_template('index.html')