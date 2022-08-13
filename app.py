from flask import Flask, request
from db import db, Developer
import json

# Flask init
app = Flask(__name__)

# DB init and config
db_filename = "session1.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/', methods=["GET"])
def greet():
    return "Hello"


@app.route('/developers/', methods=["POST"])
def create_developer():

    body =  json.loads(request.data)
    n, l = body.get("nickname"), body.get("lang")

    dev = Developer(nickname=n, lang=l)
    db.session.add(dev)
    db.session.commit()

    return "Created"

@app.route('/developers/', methods=['GET'])
def get_developers():

    res = [dev.serialize() for dev in Developer.query.all()] 
    return json.dumps(res)





    








if __name__ == '__main__':
    app.run()