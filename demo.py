import logging
from datetime import date

from flask import Flask
from flask_ask import Ask, statement, question, session


app = Flask(__name__)
ask = Ask(app, "/")


logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@app.route('/')
def homepage():
    return "this is working"

@ask.launch
def start_skill():
    start_message = "What movie would you like to watch?"
    return question(start_message)

@ask.intent("MovieIntent", convert={'moviePicked': 'movie'})
def movie_picked(moviePicked):
    return statement("Let's watch {}".format(moviePicked))

if __name__ == '__main__':
    app.run(debug=True)
