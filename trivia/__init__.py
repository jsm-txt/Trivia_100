from flask import Flask
from trivia.config import Config
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object(Config)

mongo = PyMongo(app)
db = mongo.db

from trivia.main.routes import main

app.register_blueprint(main)