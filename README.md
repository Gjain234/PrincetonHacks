# HackPrincetonProject
Create an Alexa skill that, given an activity, finds the best friends on Facebook to join you for the activity.

backend.py
1. Provide facebookUrl https://developers.facebook.com/tools/explorer.
    First get the access token, select user_about_me, user_friends, user_likes, user_location, user_photos, user_posts, user_tagged_places, user_videos, read_custom_friendlists
    Then copy the following to the next field.
    GET -> me?fields=name, photos{from{name,movies,languages, gender, events, sports, favorite_teams,likes{category, about}}}, tagged{from{name,movies, languages, gender, events, sports, favorite_teams,likes{category, about}}}
2. getHangoutSquadComments(["Musician", "English", "Japanese", "Nonprofit Organization", "Computer Company", "Finance Company"]

