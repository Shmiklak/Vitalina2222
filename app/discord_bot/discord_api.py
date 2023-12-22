from dotenv import load_dotenv
import discord
import os
import random
from app.chatgpt_ai.openai import chatgpt_response
from app.vitalina_utilities.utilities import selectRandomGif, bcolors, selectRandomVitas

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class Vitalina(discord.Client):
    async def on_ready(self):
        print("Виталина успешно запустилась на аккаунте: ", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return False
        
        for text in ['вита', 'vita', '1187685558382772254']:
            if text in message.content.lower():

                random_event = random.randint(0, 100)

                print(bcolors.OKGREEN, "ТЕКУЩАЯ ВЕРОЯТНОСТЬ: ", random_event, bcolors.ENDC)

                if random_event > 75:
                    gif = selectRandomGif()
                    await message.channel.send(gif)
                    return True
                
                if random_event > 98:
                    await message.channel.send(f"Собакам слова не давали.")


                if message.author.id == '138957703853768705':
                # # if message.author.id == '305361927415136258':
                    # if random_event < 90:
                        await message.channel.send(f"https://tenor.com/view/mother-sgnila-cute-dance-moves-bear-gif-16312770")
                        return True

                if message.content == "Виталина, голос":
                    await message.channel.send(f"Пушистый здряв")
                    return True

                if message.content == "шмик":
                    await message.channel.send(f"Сегодня я вместо него. Чем могу помочь? :pepeBusiness:")
                    return True

                if message.content == "Виталина, что ты умеешь?":
                    await message.channel.send(f"Привет! Я могу отвечать на вопросы, поддерживать беседу и просто развлекать.")
                    return True

                if message.content == "Виталина, витас":
                    photos = selectRandomVitas()
                    await message.channel.send(photos)
                    return True

                bot_response = await chatgpt_response(message.content)
                await message.channel.send(bot_response)
                return True

intents = discord.Intents.default()
intents.message_content = True
client = Vitalina(intents=intents)