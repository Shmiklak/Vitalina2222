from dotenv import load_dotenv
import os

load_dotenv()

DEV_TRIGGERS = ['наст', 'nast']
PROD_TRIGGERS = ['витал', 'vital', '1187685558382772254', 'гуталин', 'буталин']
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_CLIENT = os.getenv('DISCORD_CLIENT_ID')

MODES = {
    "normal": "NORMAL",
    "passive": "PASSIVE",
    "agressive": "AGRESSIVE",
    "very_agressive": "VERY_AGRESSIVE",
    "sleep": "SLEEP",
    "ai_only": "AI_ONLY"
}
