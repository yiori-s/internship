#coding:utf-8

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method=='POST':
		return render_template('index.html',title="Flask test", body=request.form['message'])
	else:
		return render_template('index.html',title="Flask test", body="Test")

if __name__ == "__main__":
	app.run()
