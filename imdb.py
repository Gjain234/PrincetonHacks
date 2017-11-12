import requests
import json

# put api key here
apiKey = "f3ba73ed65de9b13e01665d32af05100"

# put imdb key here
imdb_key = "318a3ddd"

# put the music key here
music_key = "c8303e90962e3a5ebd5a1f260a69b138"

g_url = "https://api.themoviedb.org/3/genre/movie/list?api_key="+apiKey

genres_r = requests.get(g_url)
genres = genres_r.content

genres_json = json.loads(genres)["genres"]


def get_data_genre(genre):
    """
    Takes a genre with first letter capitalized, e.g. "Action",
    "Drama", "Horror", "Science Fiction", "TV Movie", "War", etc
    """
    g_url2 = "https://api.themoviedb.org/3/discover/movie?with_genres="
    for gnre in genres_json:
        if gnre["name"] == genre:
            identifier = gnre["id"]
            g_url_final = g_url2 + str(identifier) + "&api_key="+apiKey
            movie_list_r = requests.get(g_url_final)
            movie_list = movie_list_r.content
            return movie_list
    return 0


def get_data_title(title):
    """
    Returns a json with the movie data. Json has fields such as "Title",
    "Year", "Genre", "Actors", etc which can be used
    """
    r = requests.get("http://www.omdbapi.com/?apikey="+imdb_key+"&plot=full&t="
                     +title)
    if r.status_code == 200:
        return r.content
    else:
        return None



def get_music_artist(artist):
    m_url = "http://api.musicgraph.com/api/v2/artist/search?api_key="+music_key
    nme = "&name="+artist
    url_final = m_url+nme
    r = requests.get(url_final)
    return r.content


def get_music_artist_similar(artist):
    m_url = "http://api.musicgraph.com/api/v2/artist/search?api_key="+music_key
    nme = "&similar_to="+artist
    url_final = m_url+nme
    r = requests.get(url_final)
    return r.content

def print_json(j):
    parse = json.loads(j)
    print (json.dumps(parse, indent=4))
    return 0
