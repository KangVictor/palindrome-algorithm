from flask import Flask, request, jsonify, url_for, redirect, render_template
import json
app = Flask(__name__)

@app.route('/words', methods = ['POST'])
def words():
	if request.is_json:
		getWord = request.get_json()
		print (getWord['words_input'])
		# checks if it there is already the word 
		f = open("words_data.txt", "r")
		read_line = ' '
		check_exist = False
		while read_line != '':
			read_line = f.readline()
			print read_line
			if read_line == (getWord['words_input']):
				check_exist = True
			if read_line == (getWord['words_input'] + '\n'):
				check_exist = True
		f.close()

		if check_exist != True:
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