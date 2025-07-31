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
    
async def isRanked(query):
    try:
        user = await getOsuUser(query)
    except:
        return None
    
    is_bro = user.ranked_beatmapset_count >= 1
    is_master = user.ranked_beatmapset_count >= 3
    is_expert = user.ranked_beatmapset_count >= 5
    is_DADDY = user.ranked_beatmapset_count >= 10

    return {
        "is_bro": is_bro,
        "is_master": is_master,
        "is_expert": is_expert,
        "is_DADDY": is_DADDY
    }

async def checkUserRoles(query):
    try: 
        user = await getOsuUser(query)
        is_russian = user.country_code in ["RU", "KZ", "UA", "BY"]
        is_ranked = user.ranked_beatmapset_count > 0

        return {
            "user": user,
            "is_russian": is_russian,
            "is_ranked": is_ranked
        }
    except:
        return None

async def getBeatmaps():
    try:
        beatmaps = api.search_beatmapsets(explicit_content="show")

        return beatmaps.beatmapsets
    except:
        return None