import os
from flask import Flask
import flask_restplus
import flask_sqlalchemy


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to my app'