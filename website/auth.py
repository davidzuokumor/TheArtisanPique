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
        # leave this empty till we can implement sign up logic
        return redirect(url_for('auth.login'))
    else:
        return render_template("signup.html",signupform=signupform)