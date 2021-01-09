from flask import Flask
app = Flask(__name__)       #  created one instance of flask --> __name__ --> main -- jr same file la run kel

#request-->mazi machine --> 5000--> wsgi ---> /welcome -->
#mazya machine chya --> 5000 -- WSGI ---> maza code-->
                                #http://localhost:5000 --> base uri --> machine and port --> server identity
@app.route("/welcome")          # http://localhost:5000/welcome     --> route --> method
def welcome_app():
    return "welcome to flask application"


if __name__ == '__main__':
    app.run(debug=True)
    #result =welcome_app()
    #print(result)

