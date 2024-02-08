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
    return None