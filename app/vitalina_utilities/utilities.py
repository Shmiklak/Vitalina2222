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

    