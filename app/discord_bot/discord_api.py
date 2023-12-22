from dotenv import load_dotenv
import discord
import os
import random
from app.chatgpt_ai.openai import chatgpt_response
from app.vitalina_utilities.utilities import selectRandomGif

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class Vitalina(discord.Client):
    async def on_ready(self):
        print("Виталина успешно запустилась на аккаунте: ", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return False
        
        for text in ['виталин', 'vitalin', '1187685558382772254']:
            if text in message.content.lower():

                random_event = random.randint(0, 100)

                if random_event > 50:
                    gif = selectRandomGif()
                    await message.channel.send(gif)
                    return True


                # if message.author.id == '395117543406436353':
                # # if message.author.id == '305361927415136258':
                #     if random_event < 50:
                #         await message.channel.send(f"https://tenor.com/view/mother-sgnila-cute-dance-moves-bear-gif-16312770")
                #         return True

                bot_response = await chatgpt_response(message.content)
                await message.channel.send(bot_response)
                return True

intents = discord.Intents.default()
intents.message_content = True
client = Vitalina(intents=intents)