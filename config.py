import os

basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    FLASK_APP = os.environ.get("FLASK_APP")
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'your_default_database_url')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
