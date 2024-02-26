import random

with open('gif_collection.txt', encoding = 'utf-8', mode = 'r') as file:
    gifs = [line.rstrip() for line in file]

def selectRandomGif():
    random_gif = random.randint(0, len(gifs) - 1)
    return gifs[random_gif]


with open('vitas_messages.txt', encoding = 'utf-8', mode = 'r') as file:
    photos = [line.rstrip() for line in file]

def selectRandomVitas():
    random_vitas = random.randint(0, len(photos) - 1)
    return photos[random_vitas]

with open('shrine.txt', encoding = 'utf-8', mode = 'r') as file:
    shrine = [line.rstrip() for line in file]

def selectRandomShrine():
    random_shrine = random.randint(0, len(shrine) - 1)
    return shrine[random_shrine]

with open('random_user.txt', encoding='utf-8', mode='r') as file:
    users = [line.rstrip() for line in file]

def selectRandomUser():
    random_user = random.randint(0, len(users) - 1)
    return users[random_user]

def getRankEmoji(Grade):
    if str(Grade) == "Grade.A":
        return "<:rankingAsmall:1211650736375468032>"
    elif str(Grade) == "Grade.B":
        return "<:rankingBsmall:1211650794643001364>"
    elif str(Grade) == "Grade.C":
        return "<:rankingCsmall:1211650833255501874>"
    elif str(Grade) == "Grade.D":
        return "<:rankingDsmall:1211650875182030868>"
    elif str(Grade) == "Grade.SH":
        return "<:rankingSHsmall:1211650952579518515>"
    elif str(Grade) == "Grade.S":
        return "<:rankingSsmall:1211650920862056499>"
    elif str(Grade) == "Grade.XH":
        return "<:rankingXHsmall:1211650992299577387>"
    elif str(Grade) == "Grade.X":
        return "<:rankingXsmall:1211651039724445768>"
    else:
        return "<:rankingFsmall:1211653378527072297>"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'