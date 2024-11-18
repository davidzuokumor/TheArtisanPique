from flask import Blueprint, request, jsonify, redirect, url_for, flash, send_from_directory
from flask_mail import Message
from werkzeug.security import generate_password_hash
from .models import User
from website import db, mail
from .forms import LoginForm, SignUpCustomer

auth = Blueprint('auth', __name__)

@auth.route('/')
def index():
    return send_from_directory('frontend/build', 'index.html')


@auth.route('/login', methods=['POST'])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        flash('Login successful!', 'success')
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"error": "Invalid credentials"}), 400

@auth.route('/logout')
def logout():
    flash('You have been logged out.', 'info')
    return "<p>Logout</p>"

@auth.route('/select_signup_role')
def select_signup_role():
    return {"message": "React will handle this route :) "}

@auth.route('/signup_customer', methods=['POST'])
def signup_customer():
    data = request.get_json()

    name = data.get('name')
    age = data.get('age')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')

    if password != confirm_password:
        return jsonify({"error": "Passwords do not match"}), 400

    user = User(
        name=name,
        age=age,
        email=email,
        password=generate_password_hash(password)
    )

    msg = Message(
        subject='Confirming Email Registration',
        sender='artisan@email.com',
        recipients=[user.email]
    )
    msg.body = 'Thank you for signing up for this account'
    mail.send(msg)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "You have registered successfully!"}), 201

@auth.route('/signup_artisan')
def signup_artisan():
    return jsonify({"message": "You have registered as an artisan successfully!"})
