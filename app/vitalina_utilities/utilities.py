import random

with open('gif_collection.txt', encoding = 'utf-8', mode = 'r') as file:
    gifs = [line.rstrip() for line in file]

def selectRandomGif():
    random_gif = random.randint(0, len(gifs))
    return gifs[random_gif]