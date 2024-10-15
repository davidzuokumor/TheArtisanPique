from flask import Flask, render_template, request, redirect, url_for, Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
  return '<h1>Home Page</h1>'

@routes.route('/about')
def about():
  return "<h1>About Page</h1>"

