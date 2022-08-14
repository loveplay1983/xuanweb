# _*_ coding: utf-8 _*_

"""
 author: Xiong Min Xuan
 study, study, and study!!!
"""
from conf import db


# Models - database table
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)

    # optional
    def __repr__(self):
        return "<Note {0!r}>".format(self.body)


# one - many
"""
One author can write many articles
"""


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    phone = db.Column(db.String(20))
    articles = db.relationship("Article")

    def __repr__(self):
        return "<Author {0!r}>".format(self.name)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))

    def __repr__(self):
        return "<Article {0!r}>".format(self.title)


# many - one
class Citizen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    city_id = db.Column(db.Integer, db.ForeignKey("city.id"))
    city = db.relationship("City")

    def __repr__(self):
        return "<Citizen {0!r}>".format(self.name)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)

    def __repr__(self):
        return "<City {0!r}>".format(self.name)


# one - one
class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    capital = db.relationship("Capital", back_populates="country" \
                              , uselist=False)

    def __repr__(self):
        return "<Country {0!r}>".format(self.name)


class Capital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey("country.id"))
    country = db.relationship('Country', back_populates='capital')

    def __repr__(self):
        return "<Capital {0!r}>".format(self.name)


# many to many with association table
association_table = db.Table("association" \
                             , db.Column("student_id", db.Integer, db.ForeignKey("student.id")) \
                             , db.Column("teacher_id", db.Integer, db.ForeignKey("teacher.id"))
                             )


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    grade = db.Column(db.String(20))
    teachers = db.relationship("Teacher" \
                               , secondary=association_table \
                               , back_populates="students")

    def __repr__(self):
        return "<Student {0!r}>".format(self.name)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    office = db.Column(db.String(20))
    students = db.relationship("Student" \
                              , secondary=association_table \
                              , back_populates="teachers")

    def __repr__(self):
        return "<Teacher {0!r}>".format(self.name)


# one to many, bidirectional relationship
class Writer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    books = db.relationship("Book", back_populates="writer")

    def __repr__(self):
        return "<Writer {0!r}>".format(self.name)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    writer_id = db.Column(db.Integer, db.ForeignKey("writer.id"))
    writer = db.relationship("Writer", back_populates="books")

    def __repr__(self):
        return "<Book {0!r}>".format(self.name)


# one to many, bidirectional relationship - backref instead of collection
class Singer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    songs = db.relationship("Song", backref="singer")

    def __repr__(self):
        return '<Singer {0!r}>'.format(self.name)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    singer_id = db.Column(db.Integer, db.ForeignKey("singer.id"))

    def __repr__(self):
        return '<Song {0!r}>'.format(self.name)


# Cascade
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.Text)
    comments = db.relationship("Comment", back_populates="post" \
                               , cascade="all, delete-orphan")


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    post = db.relationship("Post", back_populates="comments")
