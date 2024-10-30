from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from .database_connections import get_db_connection

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TheAP'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:Project1234@localhost:3306/artisandb'
    db.init_app(app)

    @app.before_request
    def before_request():
        g.mysql_db = get_db_connection()
        g.mysql_cursor = g.mysql_db.cursor()

    @app.teardown_request
    def teardown_request(exception):
        mysql_db = getattr(g, 'db', None)
        if mysql_db is not None:
            mysql_db.close()

    migrate = Migrate(app, db)

    csrf = CSRFProtect(app)
    csrf.init_app(app)

    from .routes import routes
    from .auth import auth
    from .models import User , Product , Category

    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')


    return app