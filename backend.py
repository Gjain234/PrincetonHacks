'''
Usage:
1. Provide facebookUrl https://developers.facebook.com/tools/explorer.
    GET -> me?fields=name, photos{from{name,languages, gender, events, sports, favorite_teams,likes{category, about}}}, tagged{from{name,languages, gender, events, sports, favorite_teams,likes{category, about}}}
2. getHangoutSquadComments(["Musician", "English", "Japanese", "Nonprofit Organization", "Computer Company", "Finance Company"]


'''


import requests
import collections
import operator

# max num friends suggested
MAX_FRIENDS = 5
# facebook JSON: me?fields=name, photos{from{name,languages, gender, events, sports, favorite_teams,likes{category, about}}}, tagged{from{name,languages, gender, events, sports, favorite_teams,likes{category, about}}}
facebookUrl = "https://graph.facebook.com/v2.11/me?fields=name%2C%20photos%7Bfrom%7Bname%2Clanguages%2C%20gender%2C%20events%2C%20sports%2C%20favorite_teams%2Clikes%7Bcategory%2C%20about%7D%7D%7D%2C%20tagged%7Bfrom%7Bname%2Clanguages%2C%20gender%2C%20events%2C%20sports%2C%20favorite_teams%2Clikes%7Bcategory%2C%20about%7D%7D%7D&access_token=EAACEdEose0cBANDwrRiyjLvZCZAYo1QocB1gjVKScishwZB1af6nT2QxPuTaPEoaxNSiF1i7gbZAMZCOMcGDDIx2SRSZCBVnsyPsG8KLFUFsJ2pQjuzmzcDZBzkNbIjfWchGJnP3ZAFOAB4ZCXTVdZCnrEtPRZBvUst0ylWIAC5ObiEtdAODa8vJTli0lh21SgQGVDoaeBSxhApLgZDZD"                                                                                                        # <---  put your fb URL here

commentList = dict()
def addComment(comment, name):
    '''
    Add comment to the list.
    :param comment: comment added
    :param name: name of the friend
    :return:
    '''
    if name in commentList:
        if len(commentList[name]) < 100:
            commentList[name] += comment
    else:
        commentList[name] = comment

def parseDicts(peopleTagged, peopleList, activity, scoreList, myName):
    '''
    Parses the dictionaries to find the top relevant friends and add the comments correspondingly.
    :param peopleTagged: People who are tagged in your photo.
    :param peopleList: People name list
    :param activity: Keywords
    :param scoreList: Scores of relevance
    :param myName: user's name
    :return:
    '''
    for data in peopleTagged:
        # if "likes" in data:
        #NAME = data["from"]["name"]

        # don't count about yourself
        if data["from"]["name"] == myName:
            continue

        # don't count the same person twice
        if data["from"]["name"] in peopleList:
            continue


        peopleList[data["from"]["name"]] += 1
        addComment("You and " + data["from"]["name"] + " are tagged in the same photo before.", data["from"]["name"])

        if 'likes' in data["from"]:
            # print(data["from"]["likes"]['data'])
            #print("===============================")
            #print(data["from"]["name"])
            name = data["from"]["name"]
            #print("this person likes:")
            for page in data["from"]["likes"]['data']:

                if "category" in page:
                    for act in activity:
                        act = act.lower()
                        if 'event' in data["from"]:
                            if act in data['from']['event']["data"]["discription"]:
                                scoreList[name] += 1

                                addComment("You both like to attend events about "+data['from']['event']["data"]["discription"]+".", name)
                        if 'language' in data["from"]:
                            if act in data["from"]['language']:
                                scoreList[name] += 1
                                addComment("They speak "+data["from"]['language']+".", name)
                        if 'sports' in data["from"]:
                            if act in data["from"]['sports']:
                                scoreList[name] += 1
                                addComment("They like" + data["from"]['sports'] + ".", name)
                        if 'favorite_teams' in data["from"]:
                            for team in data["from"]['favorite_teams']:
                                teamString = "Their favorite sports teams are "
                                if act in team['data']['name']:
                                    scoreList[name] += 1
                                    teamString+= team['data']['name']
                                addComment(teamString, name)

                        if act in page['category'].lower():
                            scoreList[name] += 1
                            addComment("They like to attend events in " + page['category'].lower() + " categoty.", name)
                    # actList[name] = page['category']
                    print(page['category'])
                if "about" in page:
                    for act in activity:
                        act = act.lower()
                        if act in page['about'].lower():
                            scoreList[name] += 1
                    #aboutList[name] = page['about']
    return peopleList,scoreList

def getRosterFromFB(activity):
    '''

    :param activity:
    :return:
    '''
    info = requests.get(facebookUrl).json()
    myName = info["name"]
    photos = info["photos"]
    #tagged = info["tagged"]
    peopleTagged = photos["data"]
    #peopleWhoTagMe = tagged["data"]
    peopleList = collections.Counter()

    #aboutList = collections.Counter()
    scoreList = peopleList
    peopleList, scoreList = parseDicts(peopleTagged, peopleList, activity, scoreList, myName)
    #peopleList, scoreList = parseDicts(peopleWhoTagMe, peopleList, activity, scoreList, myName)
    scores = sorted(scoreList.items(), key=operator.itemgetter(1), reverse = True)
    names = []

    for i in range(min(MAX_FRIENDS, len(scores))):
        names.append(scores[i])
    #print("names collected.")
    return names



def getMessage(squadRoster):
    '''

    :param squadRoster:
    :return:
    '''

    message = "You might want to hangout with "
    for m in squadRoster:
        message += (m[0] + ', ')
    #print(commentList)
    message += "but " + squadRoster[0][0] + " has some sincere passion in these activities. " + str(commentList[squadRoster[0][0]])

    return message


def getHangoutSquadComments(activity):
    '''

    :param activity:
    :return: Messages for Alexa to -READ OUT LOUD-.
    '''
    #print("activity: {0}".format(activity))

    # get your squad roster from fb
    squadRoster = getRosterFromFB(activity)

    # get messages
    alexaMessage = getMessage(squadRoster)
    return alexaMessage

#print(commentList)
#print(getHangoutSquadComments(["Musician", "English", "Japanese", "Dance", "Indian"]))
