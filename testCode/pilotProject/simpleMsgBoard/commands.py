# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""
import click

from simpleMsgBoard import app, db
from simpleMsgBoard.models import Message
from faker import Faker


@app.cli.command()
@click.option("--drop", is_flag=True, help="Create after drop.")
def initdb(drop):
    if drop:
        click.confirm("This operation will delete the database, \
        do you want to continue?", abort=True)
        db.drop_all()
        click.echo("Drop tables.")
    db.create_all()
    click.echo("Database is initialized.")


@app.cli.command()
@click.option("--count", default=20, help="Quantity of messages, default 20")
def forge(count):
    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo("Working...")

    for each in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo(f"Created {count} fake messages.")
