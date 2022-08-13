from flask import Flask, request
from db import db, Developer
import json

# Flask init
app = Flask(__name__)

# DB init and config
db_filename = "te_one.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/', methods=["GET"])
def greet():
    return "Hello"


@app.route('/developers/', methods=['GET'])
def get_developers():
    """ Get all developers """
    res = [dev.serialize() for dev in Developer.query.all()] 
    return json.dumps(res)


@app.route('/developers/', methods=["POST"])
def create_developer():
    """ Create a developer """

    body =  json.loads(request.data)
    n, l = body.get("nickname"), body.get("language")

    dev = Developer(nickname=n, language=l)
    db.session.add(dev)
    db.session.commit()

    return "Created"



if __name__ == '__main__':
    app.run()