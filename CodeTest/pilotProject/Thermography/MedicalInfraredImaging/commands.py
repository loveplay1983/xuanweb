# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""
import click

from MedicalInfraredImaging import app, db
from MedicalInfraredImaging.models import Patient, UploadImage, MedRecord, InitClinic, DocClinic


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Patient=Patient, UploadImage=UploadImage,
                MedRecord=MedRecord, InitClinic=InitClinic, DocClinic=DocClinic)


@app.cli.command()
@click.option("--drop", is_flag=True, help="Create after drop.")
def initdb(drop):
    """
    Initialize the database.
    """
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("Database     is initialized!")
