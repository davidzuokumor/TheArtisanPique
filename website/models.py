from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(120))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
    products = db.relationship('Product', backref='author', lazy=True)

    def __str__(self):
        return self.name , self.age , self.date_created

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(40), nullable=False)
    product_description = db.Column(db.String(80), nullable=False)
    product_price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    uploaded = db.Column(db.DateTime(timezone=True),default=func.now())

    def __str__(self):
        return self.product_name , self.product_price

class Category(db.Model):
    cat_id = db.Column(db.Integer,primary_key=True,nullable=False)
    category_name = db.Column(db.String(30),nullable=False,unique=True)
    product_id = db.relationship('Product',backref='category',lazy=True)

    def __str__(self):
        return self.category_name
