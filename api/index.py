from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upcoming')
def upcoming():
    return render_template('upcoming.html')
    
@app.route('/about')
def about():
    return 'About'

if __name__ == '__main__':
    app.run(debug=True, port=8000)