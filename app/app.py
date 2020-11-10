import os

from flask import Flask

BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASEDIR, 'db.sqlite')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from .routes import *  # noqa
