import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def get_random_image(width=800, height=600):
    url = f"https://picsum.photos/{width}/{height}"
    response = requests.get(url)
    return Image.open(BytesIO(response.content)).convert("RGBA")

def add_text_to_image(img: Image.Image, text, position=(10, 10), font_size=40):
    txt = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt)

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    draw.text(position, text, fill=(255, 255, 255, 255), font=font)
    return Image.alpha_composite(img, txt)

    