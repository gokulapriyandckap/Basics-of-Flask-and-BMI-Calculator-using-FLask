from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'This is My First Flask app' 'Yay! ;)'


@app.route('/greeting')
def greetings():
    return 'Welcome To my First Flask app ;)'

# Handling the HTTP request , POST and GET Methods and also Practiced this in Postman.
@app.route('/method', methods=['GET','POST'])
def method():
    if request.method == 'POST':
        return "You've used the Post Method!"
    else:
        return "You've Used the Get Method!"

app.run()
