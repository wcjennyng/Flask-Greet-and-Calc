from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    return 'welcome'

@app.route('/welcome/back')
def say_welcomeback():
    return 'welcome back'

@app.route('/welcome/home')
def say_welcomehome():
    return 'welcome home'

