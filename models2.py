from flask_sqlalchemy import SQLAlchemy

db2 = SQLAlchemy()

class Product(db2.Model):
    id = db2.Column(db2.Integer, primary_key=True)
    name = db2.Column(db2.String(80), unique=False, nullable=False)
    price = db2.Column(db2.Float, unique=False,nullable=False)
    description = db2.Column(db2.String(120), unique=False, nullable=False)
    stock = db2.Column(db2.Integer, unique=False,nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'
