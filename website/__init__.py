from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TheAP'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME
    db.init_app(app)

    from .routes import routes
    from .auth import auth
    from .models import User , Product , Category

    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    return app