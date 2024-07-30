from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'
@app.route('/login')
def login():
    return render_template('login.html')

#internal API
@app.route('/api/v1/login_ver', methods=['POST'])
def Verify_Login():
    login_credentials = request.json()
    user_email = login_credentials['email']
    user_password = login_credentials['password']
    return 'Login'
if __name__ == '__main__':
    app.run(debug=True)
