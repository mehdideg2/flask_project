import os
from flask import Flask
import flask_restplus
import flask_sqlalchemy
from _01_simple import app
from _02_html_inside_view import app
from _03_template_str_inside_view import app


if __name__ == "__main__":
    app.debug = True
    host = os.environ.get('IP', '127.0.0.1')
    app.run(host, 5000)
