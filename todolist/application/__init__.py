from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

from os import getenv

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DB_URI')
app.config['SECRET_KEY'] = getenv('SKEY') 

db = SQLAlchemy(app)

from application import routes
