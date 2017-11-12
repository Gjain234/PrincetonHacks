import imdb
import backend
import json

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

specificMovieTrans = dict()
specificMovieTrans["S3"] = "S8"

specificMusicTrans = dict()
specificMusicTrans["S4"]="S8"

specificGenreTrans = dict()
specificGenreTrans["S6"]="S8"

enterGenre = ""
enterMovie = ""
enterBand = ""
keyWordList = []


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

@ask.intent("SpecificMovieIntent", convert={'moviePicked': 'movie'})
def movie_picked(moviePicked):
    global enterMovie
    enterMovie = moviePicked
    #print("Enter MOVIE is " + enterMovie)
    session.attributes['state'] = specificMovieTrans[session.attributes['state']]
    round_msg = render_template(session.attributes['state'])
    if(session.attributes['state'] == endState):
        return statement(round_msg)
    else:
        return question(round_msg)

@ask.intent("MusicIntent", convert={'bandPicked': 'MusicGroup'})
def band_picked(bandPicked):
    global enterBand
    enterBand = bandPicked
    session.attributes['state'] = specificMusicTrans[session.attributes['state']]
    round_msg = render_template(session.attributes['state'])
    if(session.attributes['state'] == endState):
        return statement(round_msg)
    else:
        return question(round_msg)

@ask.intent("GenreIntent", convert={'specificGenre': 'Genre'})
def genre_picked(specificGenre):
    global enterGenre
    enterGenre = specificGenre
    session.attributes['state'] = specificGenreTrans[session.attributes['state']]
    round_msg = render_template(session.attributes['state'])
    if(session.attributes['state'] == endState):
        return statement(round_msg)
    else:
        return question(round_msg)

@ask.intent("ContinueIntent")
def continue_intent():
    if(enterMovie!=""):
        movieTitle = imdb.get_data_title(enterMovie)
        js = json.loads(movieTitle)
        keyWordList.append(js["Title"])
        keyWordList.append(js["Genre"])
        keyWordList.append(js["Director"])
        keyWordList.append(js["Actors"])
    elif(enterGenre!=""):
        keyWordList.append(enterGenre)
    elif(enterBand!=""):
        artist = imdb.get_music_artist(enterBand)
        js = json.loads(artist)
        keyWordList.append(js["data"][0]["main_genre"])
        keyWordList.append(js["data"][0]["name"])
        #similarArtists = imdb.get_music_artist_similar(enterBand)
        #js2 = json.loads(similarArtists)

#print("LOOKING FOR ERRORS WE ARE PRINTING RIGHT NOW!!!!!!!!!!!!!!!!!!!!!!!!")
#print(enterMovie)
#print (len(keyWordList))
#for x in keyWordList:
#print (x)
    
    alexaMessage = backend.getHangoutSquadComments(keyWordList)
    return statement(alexaMessage)




if __name__== '__main__':
    app.run(debug = True)
