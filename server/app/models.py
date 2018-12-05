from app import db
from datetime import datetime


# Таблица с пользователями в базе
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(128), unique=True, index=True)
    password = db.Column(db.String(128))
    projects = db.relationship('Project', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


# Таблица с проектами в базе
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(128), unique=True)
    describe = db.Column(db.String(1000))
    startDate = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    endDate = db.Column(db.DateTime)

    def __repr__(self):
        return '<Project {0}, start {1}>'.format_map(self.title, self.startDate)
