from flask import Flask, request
from db import db, Developer

# Flask Init
app  = Flask(__name__)

# DB init and config
db_filename = "session2.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
db.init_app(app)
with app.app_context():
    db.create_all()



# Go to homepage
@app.route('/', methods=['GET'])
def home():
    return "Hello Developer! You are welcome!"














# Decides the part of the code to be run when executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4500)
