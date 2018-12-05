from app import db
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash


# Таблица с пользователями в базе
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(128), unique=True, index=True)
    password = db.Column(db.String(128))
    projects = db.relationship('Project', backref='user', lazy='dynamic')

    # хеширование пароля
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # сравнение хешей паролей
    def check_password(self, password):
        return check_password_hash(self.password, password)

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
    tasks = db.relationship('Task', backref='project', lazy='dynamic')

    def __repr__(self):
        return '<Project {0}, start {1}>'.format_map(self.title, self.startDate)


# Таблица с задачами по проектам
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idProject = db.Column(db.Integer, db.ForeignKey('project.id'))
    title = db.Column(db.String(128), index=True)
    describe = db.Column(db.String(1000), nullable=False)
    status = db.Column(db.String(64), index=True, nullable=False)
    createDate = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    startDate = db.Column(db.DateTime, index=True)
    endDate = db.Column(db.DateTime)

    def __repr__(self):
        return '<Task {0}\t, create {1}\t, status {2}>'.format(self.title, self.createDate, self.status)
