from flask import Flask, request, jsonify, url_for, redirect, render_template
import json
app = Flask(__name__)

"""
Update palindrome DB with unique words (no duplicatrs allowed)

return: True if update DB, false if duplicate found
"""
@app.route('/words', methods = ['POST'])
def words():
	if request.is_json:
		# get our json from request
		getWord = request.get_json()

		# connection to our DB
		f = open("words_data.txt", "r")

		# check for duplicates
		read_line = ' '
		check_exist = False
		while read_line != '':
			read_line = f.readline()
			if read_line == (getWord['words_input']):
				check_exist = True
			if read_line == (getWord['words_input'] + '\n'):
				check_exist = True
		f.close()

		# write to DB (if duplicate word not found)
		if check_exist != True:
			# write words_input on words_data.txt
			f = open("words_data.txt","a+")
			f.write("\n%s" % getWord['words_input'])
			f.close()
		if check_exist:
			return 'true'
		else:
			return 'false'
	return "input not json"


@app.route('/palindrome/')
def palindrome():
	return render_template('Palindrome_Algorithm_02.js')

@app.route('/')
def basic():
	f = open("words_data.txt", "w+")
	f.write("palindrome words")
	f.close()
	return render_template('index.html')