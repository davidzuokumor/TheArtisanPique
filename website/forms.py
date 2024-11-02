from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField , BooleanField, ValidationError , TextAreaField , IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange, Regexp, Optional


class SignUpCustomer(FlaskForm):
    name = StringField('Enter your preferred Name',validators=[DataRequired(), Length(min=5, max=50)])
    age = IntegerField('Enter your age',validators=[NumberRange(min=17)])
    email = StringField('Enter your preferred Email',validators=[DataRequired(), Email()])
    password = PasswordField('Enter your password',validators=[DataRequired(),Length(min=8, max=12),Regexp("^[a-zA-Z0-9_]*$", message="Password must contain only letters, numbers, and underscores.")])
    confirm_password = PasswordField('Confirm your Password',validators=[DataRequired(), EqualTo("password", message="Passwords must match.")])
    submit = SubmitField('Submit and Sign Up')

class SignUpArtisan(FlaskForm):
    name = StringField('Enter your preferred Name',validators=[DataRequired(), Length(min=5, max=50)])
    age = IntegerField('Enter your age',validators=[NumberRange(min=18)])
    email = StringField('Enter your preferred Email',validators=[DataRequired(), Email()])
    password = PasswordField('Enter your password',validators=[DataRequired(),Length(min=8, max=12),Regexp("^[a-zA-Z0-9_]*$", message="Password must contain only letters, numbers, and underscores.")])
    confirm_password = PasswordField('Confirm your Password',validators=[DataRequired(), EqualTo("password", message="Passwords must match.")])

    bio = TextAreaField('Tell us about yourself', validators=[Optional(), Length(max=500)])
    skills = StringField('List your skills or expertise (Recommended)', validators=[Optional(), Length(max=100)])

    submit = SubmitField('Submit and Sign Up')

class SignUpDelivery(FlaskForm):
    pass


class LoginForm(FlaskForm):
    pass
