from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_mail import Message
from werkzeug.security import generate_password_hash
from .forms import LoginForm, SignUpCustomer
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

@auth.route('/select_signup_role')
def select_signup_role():
    return render_template("select_signup_role.html")

@auth.route('/signup_customer', methods=['GET', 'POST'])
def signup_customer():
    signup_form = SignUpCustomer()
    if signup_form.validate_on_submit():
        user = User(
               name=signup_form.name.data,
               age=signup_form.age.data,
               email=signup_form.email.data,
               password=generate_password_hash(signup_form.password.data)
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

        flash('You have registered successfully!', 'success')
        return redirect(url_for('auth.login'))

    return render_template("signup_customer.html", form=signup_form)

@auth.route('/signup_artisan')
def signup_artisan():
    return render_template("signup_artisan.html")

@auth.route('/signup_delivery_personnel')
def signup_delivery_personnel():
    return render_template("signup_delivery_personnel.html")
