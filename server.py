from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__)

@app.route('/words', methods = ['POST'])
def words():
	if request.method == 'POST':
		if request.form['words_input']:
			return {'foo': 'successful'}
		else:
			return {'foo': 'wrong input'}
	else:
		return {'foo': 'no input'}

@app.route('/')
def basic():
	return render_template('index.html')