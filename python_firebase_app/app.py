from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase

app = Flask(__name__)
app.secret_key = "super_secret_key" # Replace with proper secret in production

# Firebase Configuration
firebaseConfig = {
  "apiKey": "AIzaSyADX7F1MwQ0Q51GL_OXvyEi5aQ178LZZCc",
  "authDomain": "car-rental-a80f5.firebaseapp.com",
  "databaseURL": "https://car-rental-a80f5-default-rtdb.firebaseio.com",
  "projectId": "car-rental-a80f5",
  "storageBucket": "car-rental-a80f5.firebasestorage.app",
  "messagingSenderId": "891001606405",
  "appId": "1:891001606405:web:d85af9d8344aa4370fe76c",
  "measurementId": "G-D36Y7TX4WC"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()

@app.route('/')
def index():
    vehicles_data = db.child("vehicles").get().val()
    if not vehicles_data:
        vehicles_data = {}
    elif isinstance(vehicles_data, list):
        # Firebase sometimes returns sequential numerical keys as a list.
        # We convert it back to a dictionary, ignoring any null items.
        vehicles_data = {str(i): v for i, v in enumerate(vehicles_data) if v is not None}
        
    return render_template('index.html', vehicles=vehicles_data)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        session['user'] = user['idToken']
        return redirect(url_for('index'))
    except Exception as e:
        return f"Login failed: {e}", 400

@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('emailid')
    password = request.form.get('password')
    try:
        user = auth.create_user_with_email_and_password(email, password)
        session['user'] = user['idToken']
        return redirect(url_for('index'))
    except Exception as e:
        return f"Registration failed: {e}", 400

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
