from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Developer(db.Model):
    __tablename__ = 'developers'
    id = db.Column(db.Integer, primary_key = True)
