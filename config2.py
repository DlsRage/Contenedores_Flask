import os

class Config2:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgresql://myuser2:mypassword2@db2:5432/products'
    SQLALCHEMY_TRACK_MODIFICATIONS = False