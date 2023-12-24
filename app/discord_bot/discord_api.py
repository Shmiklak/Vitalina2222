from dotenv import load_dotenv
import discord
import os
import random
from app.chatgpt_ai.openai import chatgpt_response
from app.vitalina_utilities.utilities import selectRandomGif, bcolors, selectRandomVitas, selectRandomShrine

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class Vitalina(discord.Client):
    async def on_ready(self):
        print("Виталина успешно запустилась на аккаунте: ", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return False
        
        if message.content == "шмик":
            await message.channel.send(f"Сегодня я вместо него. Чем могу помочь? :pepeBusiness:")
            return True
        
        random_event = random.randint(0, 100)
        print(bcolors.OKGREEN, "ТЕКУЩАЯ ВЕРОЯТНОСТЬ: ", random_event, bcolors.ENDC)

        if message.author.id == 305361927415136258:
            if random_event > 95:
                await message.channel.send(f"https://tenor.com/view/mother-sgnila-cute-dance-moves-bear-gif-16312770")
                return True

        for text in ['вита', 'vita', '1187685558382772254']:
            if text in message.content.lower():

                if message.content == "Виталина, голос":
                    await message.channel.send(f"Пушистый здряв")
                    return True

                if message.content == "Виталина, что ты умеешь?":
                    await message.channel.send(f"Привет! Я могу отвечать на вопросы, поддерживать беседу и просто развлекать.")
                    return True

                if message.content == "Виталина, у нас новенькие":
                    await message.channel.send(f"Привет! Основная информация по тому или иному каналу указана в его шапке! Если у тебя возникли вопросы, не стесняйся задавать их в чатике, а теперь - вперед навстречу ярким эмоциям! :pepeBusiness:")
                    return True

                if message.content == "Виталина, ранкни карту":
                    await message.channel.send(f"Конечно, отправь карту в мою очередь: https://docs.google.com/forms/d/e/1FAIpQLSdn1i6C44nSaxSQRyEeL3_jvXrxFn-U0hAfxUkTYIudatmiTA/viewform?usp=sf_link")
                    return True

                if message.content == "Виталина, скинь смешнявку":
                    shrine = selectRandomShrine()
                    await message.channel.send(shrine)
                    return True

                if message.content == "Виталина, витас":
                    photos = selectRandomVitas()
                    await message.channel.send(photos)
                    return True
                
                if random_event > 75:
                    gif = selectRandomGif()
                    await message.channel.send(gif)
                    return True
                
                if random_event > 98:
                    await message.channel.send(f"Собакам слова не давали.")

                bot_response = await chatgpt_response(message.content)
                await message.channel.send(bot_response)
                return True

intents = discord.Intents.default()
intents.message_content = True
client = Vitalina(intents=intents)