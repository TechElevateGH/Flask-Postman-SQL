from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Developer(db.Model):
    __tablename__ = 'developers'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String)
    lang = db.Column(db.String)


    def serialize(self):
        return ({
            "id" : self.id,
            "name" : self.nickname,
            "lang" : self.lang
        })
