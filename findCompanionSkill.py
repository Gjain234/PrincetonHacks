import logging
import os
from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

BeginState = "S1"
endState = "S8"

movieTrans = dict()
movieTrans["S1"] = "S2"

yesTrans = dict()
yesTrans["S2"] = "S3"

noTrans = dict()
noTrans["S2"] = "S6"

concertTrans = dict()
concertTrans["S1"] = "S4"

sportsTrans = dict()
sportsTrans["S1"] = "S5"

basketballTrans = dict()
basketballTrans["S5"] = "S7"

baseballTrans = dict()
baseballTrans["S5"] = "S7"

footballTrans = dict()
footballTrans["S5"] = "S7"

tennisTrans = dict()
tennisTrans["S5"] = "S7"

golfTrans = dict()
golfTrans["S5"] = "S7"

volleyballTrans = dict()
volleyballTrans["S5"] = "S7"

hockeyTrans = dict()
hockeyTrans["S5"] = "S7"

specificMovieTrans = dict()
specificMovieTrans["S3"] = "S8"


@ask.launch
def start_skill():
    session.attributes['state'] = BeginState
    start = render_template(session.attributes['state'])
    return question(start)

@ask.intent("MovieIntent")
def movie_intent():
    session.attributes['state'] = movieTrans[session.attributes['state']]
    round_msg = render_template(session.attributes['state'])
    if(session.attributes['state'] == endState):
        return statement(round_msg)
    else:
        return question(round_msg)

@ask.intent("YesIntent")
def yes_intent():
    session.attributes['state'] = yesTrans[session.attributes['state']]
    round_msg = render_template(session.attributes['state'])
    if(session.attributes['state'] == endState):
        return statement(round_msg)
    else:
        return question(round_msg)

@ask.intent("NoIntent")
def no_intent():
    session.attributes['state'] = noTrans[session.attributes['state']]
    round_msg = render_template(session.attributes['state'])
    if(session.attributes['state'] == endState):
        return statement(round_msg)
    else:
        return question(round_msg)

@ask.intent("ConcertIntent")
def concert_intent():
    session.attributes['state'] = concertTrans[session.attributes['state']]
    round_msg = render_template(session.attributes['state'])
    if(session.attributes['state'] == endState):
        return statement(round_msg)
    else:
        return question(round_msg)

@ask.intent("SportsIntent")
def sports_intent():
    session.attributes['state'] = sportsTrans[session.attributes['state']]
    round_msg = render_template(session.attributes['state'])
    if(session.attributes['state'] == endState):
        return statement(round_msg)
    else:
        return question(round_msg)

@ask.intent("BasketballIntent")
def basketball_intent():
    session.attributes['state'] = basketballTrans[session.attributes['state']]
    round_msg = render_template(session.attributes['state'])
    if(session.attributes['state'] == endState):
        return statement(round_msg)
    else:
        return question(round_msg)

@ask.intent("BaseballIntent")
def baseball_intent():
    session.attributes['state'] = baseballTrans[session.attributes['state']]
    round_msg = render_template(session.attributes['state'])
    if(session.attributes['state'] == endState):
        return statement(round_msg)
    else:
        return question(round_msg)

@ask.intent("FootballIntent")
def football_intent():
    session.attributes['state'] = footballTrans[session.attributes['state']]
    round_msg = render_template(session.attributes['state'])
    if(session.attributes['state'] == endState):
        return statement(round_msg)
    else:
        return question(round_msg)

@ask.intent("TennisIntent")
def tennis_intent():
    session.attributes['state'] = tennisTrans[session.attributes['state']]
    round_msg = render_template(session.attributes['state'])
    if(session.attributes['state'] == endState):
        return statement(round_msg)
    else:
        return question(round_msg)

@ask.intent("GolfIntent")
def golf_intent():
    session.attributes['state'] = golfTrans[session.attributes['state']]
    round_msg = render_template(session.attributes['state'])
    if(session.attributes['state'] == endState):
        return statement(round_msg)
    else:
        return question(round_msg)

@ask.intent("VolleyballIntent")
def volleyball_intent():
    session.attributes['state'] = volleyballTrans[session.attributes['state']]
    round_msg = render_template(session.attributes['state'])
    if(session.attributes['state'] == endState):
        return statement(round_msg)
    else:
        return question(round_msg)

@ask.intent("HockeyIntent")
def hockey_intent():
    session.attributes['state'] = hockeyTrans[session.attributes['state']]
    round_msg = render_template(session.attributes['state'])
    if(session.attributes['state'] == endState):
        return statement(round_msg)
    else:
        return question(round_msg)

@ask.intent("SpecificMovieIntent", convert={'moviePicked': 'movie'})
def movie_picked(moviePicked):
    session.attributes['state'] = specificMovieTrans[session.attributes['state']]
    return statement("Looking for people to watch {} with.".format(moviePicked))

if __name__== '__main__':
    app.run(debug = True)
