from flask import Flask, render_template, request, Response

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hosp Rapido'


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)