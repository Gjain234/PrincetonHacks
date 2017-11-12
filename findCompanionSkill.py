import logging
import os
from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

BeginState = "S1"
endState = "S7"

movieTrans = dict()
movieTrans["S1"] = "S2"

concertTrans = dict()
concertTrans["S1"] = "S3"

sportsTrans = dict()
sportsTrans["S1"] = "S4"

basketballTrans = dict()
basketballTrans["S4"] = "S6"

baseballTrans = dict()
baseballTrans["S4"] = "S6"

footballTrans = dict()
footballTrans["S4"] = "S6"

tennisTrans = dict()
tennisTrans["S4"] = "S6"

golfTrans = dict()
golfTrans["S4"] = "S6"

volleyballTrans = dict()
volleyballTrans["S4"] = "S6"

hockeyTrans = dict()
hockeyTrans["S4"] = "S6"



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

if __name__== '__main__':
    app.run(debug = True)
