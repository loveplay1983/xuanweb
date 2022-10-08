# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""

from flask import make_response, render_template, \
    redirect, url_for
from MedicalInfraredImaging import app


@app.errorhandler(404)
def not_found(e):
    """Page not found."""
    return make_response(
        render_template("errors/404.html"),
        404
    )


@app.errorhandler(400)
def bad_request(e):
    """Bad request."""
    return make_response(
        render_template("errors/400.html"),
        400
    )


@app.errorhandler(500)
def server_error(e):
    """Internal server error."""
    return make_response(
        render_template("errors/500.html"),
        500
    )


@app.route("/errors/duplicated-patient-id")
def duplicatedPatientID():
    return render_template("errors/duplicatedID.html")
