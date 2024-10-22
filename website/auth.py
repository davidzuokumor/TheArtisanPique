from flask import Blueprint, render_template, url_for, redirect, request
from .forms import SignUpForm , LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    loginform = LoginForm()
    data = request.form

    if request.method == 'POST':
        # leave this empty for now
        print(data)
        return redirect(url_for('routes.home'))
    return render_template("login.html",loginform=loginform)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
    signupform = SignUpForm()
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        role = request.form.get('role')

        #implement validation login here and the password hashing too

        return redirect(url_for('auth.login'))
    else:
        return render_template("signup.html",signupform=signupform)