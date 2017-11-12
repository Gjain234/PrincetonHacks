import imdb
import backend

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
    enterMovie = moviePicked
    session.attributes['state'] = specificMovieTrans[session.attributes['state']]
    return statement("Looking for people to watch {} with.".format(moviePicked))

@ask.intent("MusicIntent", convert={'bandPicked': 'MusicGroup'})
def band_picked(bandPicked):
    enterBand = bandPicked
    session.attributes['state'] = specificMusicTrans[session.attributes['state']]
    return statement("Looking for people to go to {}'s concert with.".format(bandPicked))

@ask.intent("GenreIntent", convert={'specificGenre': 'Genre'})
def genre_picked(specificGenre):
    enterGenre = specificGenre
    session.attributes['state'] = specificGenreTrans[session.attributes['state']]
    return statement("Looking for people to watch {} movies with.".format(specificGenre))

@ask.intent("ContinueIntent")
def continue_intent():
    if(enterMovie!=""):
        movieTitle = imdb.get_data_title(enterMovie)
        js = json.loads(movieTitle)
        keyWordList.append(js["Title"])
        keyWordList.append(js["Genre"])
        keyWordList.append(js["Director"])
        keyWordList.append(js["Actors"])
    else if(enterGenre!=""):
        keyWordList.append(enterGenre)
    else if(enterBand!=""):
        artist = imdb.get_music_artist(enterBand)
        js = json.loads(artist)
        keyWordList.append(js["data"][0]["main_genre"])
        keyWordList.append(js["data"][0]["name"])
        #similarArtists = imdb.get_music_artist_similar(enterBand)
        #js2 = json.loads(similarArtists)




if __name__== '__main__':
    app.run(debug = True)
