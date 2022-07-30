from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Boolean

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = "Post"
    id = db.Column('id', db.String, primary_key=True)
    title = Column(String)
    author = Column(String)
    date = db.Column(Integer)
    upvotes  = Column(Integer)
    downvotes = Column(Integer)
    active = Column(Boolean)
    photo = Column(String)


    # Optional
    def __init__(self, **kwargs) -> None:
        self.author = kwargs.get('author')
        self.date = kwargs.get('date')
        self.upvotes  = kwargs.get('upvotes')
        self.downvotes = kwargs.get('downvotes')
        self.active = kwargs.get('active')
        self.photo = kwargs.get('photo')

    def serialize(self):
        return ({
            "title": self.title,
            "author": self.author,
            "date": self.date,
            "upvotes": self.upvotes
        })