from flask import Flask, request

# Flask Init
app  = Flask(__name__)


# Go to homepage
@app.route('/', methods=['GET'])
def home():
    return "Hello there! You are welcome!"






# Decides the part of the code to be run when executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4500)
