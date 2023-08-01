from flask import Flask


app = Flask(__name__)


@app.route('/')
def welcome():
    return 'This is My First Flask app' 'Yay! ;)'


@app.route('/greeting')
def greetings():
    return 'Welcome To my First Flask app ;)'




app.run()
