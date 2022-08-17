# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""

from flask import flash, redirect, url_for, render_template
from simpleMsgBoard import app, db
from simpleMsgBoard.forms import MsgForm
from simpleMsgBoard.models import Message


@app.route("/", methods=["GET", "POST"])
def index():
    form = MsgForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash("Your message have been sent to the world!")
        return redirect(url_for("index"))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template("index.html", form=form, messages=messages)


