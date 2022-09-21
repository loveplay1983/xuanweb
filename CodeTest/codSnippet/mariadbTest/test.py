# _*_coding:utf-8_*_
"""
Author: Michael Xuan
Purpose: Study
Direction: web 
"""
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as mariadb


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:xxm040506@localhost/xuan"
db = SQLAlchemy(app)


@app.route("/act", methods=["GET", "POST"])
def act():
    if (request.method == "POST"):
        try:
            name = request.form["name"]
            roll = request.form["roll"]
            conn = mariadb.connect(user="")


