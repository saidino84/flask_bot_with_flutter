from app.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password=db.Column(db.String(200),nullable=False)


    @staticmethod
    def from_json(json):
        return User(username=json['username'],email=json['email'],password=json['password'])




    def __repr__(self):
        return '<User %r>' % self.username
