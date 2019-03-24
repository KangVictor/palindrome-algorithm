from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__)

@app.route('/words', methods = ['POST'])
def words():
	if request.methods == 'POST':
		if request.form['words_input']:
			return 'input successful'
		else: 
			return 'still in'
	else:
		return 'wrong input'
	return 'hello'

@app.route('/')
def basic():
	return render_template('index.html')