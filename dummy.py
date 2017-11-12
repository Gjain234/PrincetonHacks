import imdb
def get_mv(mv):
	r = imdb.get_title_data(mv)
	js = json.loads(r)
	artists = js["Actors"]
	title = js["Title"]
	
