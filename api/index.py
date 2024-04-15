from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/test/<text>')
def test(text):
    return text
    
@app.route('/about')
def about():
    return 'About'
