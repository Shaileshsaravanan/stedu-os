from flask import Flask, render_template,request,redirect,url_for,session
from firebase_admin import credentials
from google.cloud import storage

#from dotenv import load_dotenv

#load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upcoming')
def upcoming():
    return render_template('upcoming.html')
    
@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/user/profile')
def user_profile():
    return render_template('user/profile.html')

@app.route('/signup')
def signup_page():
    return render_template('Sign_up_page.html')

@app.route("/api/v1/signup", methods=["POST"])
def create_user():
    data = request.json
    user_email = data["email"]
    user_password = data["password"]
    user_name = data["name"]
    print(user_email, user_password)
    return {"Status": "Success","code" :"200"}

@app.route('/api/v1/get/user_data')
def fetch_user_data():
    data = request.json
    user_email = data["email"]
    return render_template('user/profile.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)