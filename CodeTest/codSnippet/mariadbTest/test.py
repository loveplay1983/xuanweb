# _*_coding:utf-8_*_
"""
Author: Michael Xuan
Purpose: Study
Direction: web 
"""
import os
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.debug = True

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://xuan:pgjdcwn1983@127.0.0.1:3306/xuan"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
