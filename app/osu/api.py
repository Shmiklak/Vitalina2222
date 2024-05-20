from ossapi import Ossapi
import os

client_id = os.getenv("OSU_CLIENT_ID")
client_secret = os.getenv("OSU_CLIENT_SECRET")

api = Ossapi(client_id, client_secret)

async def getOsuUser(query, mode=""):
    if mode != "":
        return api.user(query, mode=mode)
    else:
        return api.user(query)

async def getRecentScore(user_id):
    return api.user_scores(user_id=user_id, type="recent", limit=1)

async def getBeatmap(beatmap_id):
    return api.beatmap(beatmap_id)

async def isRussian(query):
    try:
        user = api.user(query)
    except:
        return False
    
    if user.country_code in ["RU", "KZ", "UA", "BY"]:
        return True
    else:
        return False
