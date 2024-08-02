from flask import Flask, render_template,request,redirect,url_for,session
from firebase_admin import auth
import firebase_admin
import flask
from firebase_admin import credentials
from google.cloud import storage

try:
    storage_client = storage.Client.from_service_account_json('api/firestore.json')
    cred = credentials.Certificate('api/firestore.json')
except:
    storage_client = storage.Client.from_service_account_json('firestore.json')
    cred = credentials.Certificate('firestore.json')
firebase_admin.initialize_app(cred)

# from dotenv import load_dotenv
# load_dotenv()
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
    return User_login_status_deliver_content('user/profile.html')
    #return render_template('user/profile.html')

@app.route('/signup')
def signup_page():
    return User_login_status_deliver_content('Sign_up_page.html')

@app.route("/api/v1/signup", methods=["POST"])
def create_user():
    data = request.json
    user_email = data["email"]
    user_password = data["password"]
    user_name = data["name"]
    print(user_email, user_password)
    try:
        user = auth.create_user(email=user_email,email_verified=False,password=user_password,disabled=False)
        print("Successfully created new user: {0}".format(user.uid))
        return {"Status": "Success","code" :"200","email":user_email,"password":user_password}
    except Exception as e :
        print("Error Could not crate user",e)
        return {"Status": "Failed","code" :"400","Error":str(e)}

@app.route('/api/v1/get/user_data')
def fetch_user_data():
    data = request.json
    user_email = data["email"]
    return render_template('user/profile.html')

def User_login_status_deliver_content(page):
    session_cookie = flask.request.cookies.get('session')
    if not session_cookie:
        print("User Session is not valid redirecting to login page")
        return flask.redirect('/login')
    try:
        decoded_claims = auth.verify_session_cookie(session_cookie, check_revoked=True)
        print("User Session is valid returing page content")
        return render_template(page)
    except auth.InvalidSessionCookieError:
        return flask.redirect('/login')

if __name__ == '__main__':
    app.run(debug=True, port=8000)