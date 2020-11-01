from flask import Flask
app = Flask(__name__)


@app.route("/")                 #http://localhost:5000/
def welcome_method():
    return "hhi"       # list ---> python  cha -->     browser ?? generic --> object lang --> format-->

if __name__ == '__main__':
    app.run(debug=True)