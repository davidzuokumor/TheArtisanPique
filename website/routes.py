from flask import Flask, render_template, request, redirect, url_for, Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
  return render_template("index.html")

@routes.route('/about')
def about():
  return "<h1>About Page</h1>"

