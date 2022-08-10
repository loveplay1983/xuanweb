# _*_ coding: utf-8 _*_

"""
 author: Xiong Min Xuan
 study, study, and study!!!
"""
from packages import Flask, os, sys, click, SQLAlchemy

# SQLite URI compatible
WIN = sys.platform.startswith("win")
if WIN:
    prefix = "sqlite:///"  # windows
else:
    prefix = "sqlite:////"  # unix-like

# Configurations
app = Flask(__name__)
# Left and right whitespace removal
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "secret string")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", prefix + os.path.join(app.root_path, "test_.db"))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.cli.command()
@click.option("--drop", is_flag=True, help="Create after drop.")
def initdb(drop):
    """
    Initialize the database.
    """
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("Database is initialized.")
