from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_mail import Message
from werkzeug.security import generate_password_hash
from .forms import SignUpForm, LoginForm
from .models import User
from website import db, mail

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit(): 
        flash('Login successful!', 'success')
        return redirect(url_for('routes.home'))
    return render_template("login.html", loginform=loginform)

@auth.route('/logout')
def logout():
    flash('You have been logged out.', 'info')
    return "<p>Logout</p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    signupform = SignUpForm()
    if signupform.validate_on_submit(): 
        user = User(
            username=signupform.username.data,
            age=signupform.age.data,
            email=signupform.email.data,
            role=signupform.role.data,
            password=generate_password_hash(signupform.password.data)  
        )
        
        db.session.add(user)  
        db.session.commit() 
        
        
        msg = Message(
            subject='Confirming Email Registration',
            sender='artisan@email.com',
            recipients=[user.email]
        )
        msg.body = 'Thank you for signing up for this account'
        mail.send(msg)
        
        flash('You have registered successfully!', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template("signup.html", signupform=signupform)
