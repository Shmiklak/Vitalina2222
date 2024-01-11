from dotenv import load_dotenv
import discord
import os
import random
from app.chatgpt_ai.openai import chatgpt_response
from app.vitalina_utilities.utilities import selectRandomGif, bcolors, selectRandomVitas, selectRandomShrine

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

recent_senders = []
recent_messages = []
consecutive_messages = 0
required_consecutive_messages = 3


#
# NORMAL
# PASSIVE
#

vitalina_current_mode = "NORMAL"

vitalina_ignore_list = [982193341754122250, 395291663834021890]

class Vitalina(discord.Client):
    async def on_ready(self):
        print("Виталина успешно запустилась на аккаунте: ", self.user)
        await self.change_presence(activity=discord.Game(name="osu!"))

    async def on_message(self, message):
        if message.author == self.user or message.author.id in vitalina_ignore_list:
            return False
        
        if isinstance(message.channel, discord.DMChannel):
            await message.channel.send(f"Я не буду отвечать вам в личных сообщениях. Ищите меня на серверах")
            return True

        if message.content == "шмик":
            await message.channel.send(f"Сегодня я вместо него. Чем могу помочь? <:pepeBusiness:1036987708456845391>")
            return True
        
        global consecutive_messages
        global recent_senders
        global recent_messages
        global vitalina_current_mode

        if message.author.id not in recent_senders and message.content in recent_messages:
            recent_senders.append(message.author.id)
            recent_messages.append(message.content)
            consecutive_messages += 1
        else:
            recent_senders = [message.author.id]
            recent_messages = [message.content]
            consecutive_messages = 1

        if consecutive_messages == required_consecutive_messages:
            await message.channel.send(message.content)
            recent_senders = []
            recent_messages = []
            consecutive_messages = 0
    
        
        random_event = random.randint(0, 100)
        rare_events = random.randint(0, 1000)
        print(bcolors.OKGREEN, "ТЕКУЩАЯ ВЕРОЯТНОСТЬ: ", random_event, bcolors.ENDC)
        print(bcolors.OKGREEN, "ТЕКУЩАЯ РЕДКАЯ ВЕРОЯТНОСТЬ: ", rare_events, bcolors.ENDC)

        # if message.author.id == 305361927415136258 or message.author.id == 313751415061479426:
        #     if random_event > 95:
        #         await message.channel.send(f"https://tenor.com/view/mother-sgnila-cute-dance-moves-bear-gif-16312770")
        #         return True
            
        if rare_events > 998:
            await message.channel.send(f"Пока перерыв расскажу лайфхак, в бауманке придумали такую хуйню, можно пельмени не варить а употреблять прямо так, замороженые, можно перед парами пельмень аккуратно вставить в анус и идти спокойно, сразу в кишку поступают белки там, углеводы, жиры, под конец курса можно было по 5-6 пельменей помещать")
            return True

        if '1187685558382772254' in message.content:
            if random_event > 50:
                await message.channel.send(f"https://tenor.com/view/chungus-pinged-ben-shapiro-discord-big-gif-21424212")
                return True 
        
        trigger_vitalina = False

        for text in ['витал', 'vital', '1187685558382772254']:
            if text in message.content.lower():
                trigger_vitalina = True

        if message.type == discord.MessageType.reply:
            reference = await message.channel.fetch_message(message.reference.message_id)

            if reference.author.id == self.user.id:
                trigger_vitalina = True


        if trigger_vitalina:       

            ###                                 ###
            ### СИСТЕМНЫЕ КОМАНДЫ ДЛЯ ШМИКЛАКА  ###
            ###                                 ###

            if message.content.lower() == "виталина, дейлики":
                if message.author.id == 138957703853768705:
                    await message.channel.send(f"<@304470215733936148> сделай дейлики шмиклаку пожалуйста")
                    return True
                else:
                    await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                    return True
            
            if message.content.lower() == "виталина, история":
                if message.author.id == 138957703853768705:
                    bot_response = await chatgpt_response("MARVOLLO_HISTORY")
                    await message.channel.send(bot_response)
                    return True
                else:
                    await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                    return True
                
            if message.content.lower() == "виталина, сброс":
                if message.author.id == 138957703853768705:
                    bot_response = await chatgpt_response("MARVOLLO_RESET")
                    await message.channel.send(f"Виталина была сброшена с моста.<:pepeBusiness:1036987708456845391>")
                    return True
                else:
                    await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                    return True
            
            if message.content.lower() == "виталина, обычный режим":
                if message.author.id == 138957703853768705:
                    vitalina_current_mode = "NORMAL"
                    await message.channel.send("Изменила режим работы на обычный.")
                    return True
                else:
                    await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                    return True
            
            if message.content.lower() == "виталина, пассивный режим":
                if message.author.id == 138957703853768705:
                    vitalina_current_mode = "PASSIVE"
                    await message.channel.send("Изменила режим работы на пассивный.")
                    return True
                else:
                    await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                    return True
            
            ### виталина, отправляем сообщение|CHANNEL_ID|MESSAGE

            if "виталина, отправляем сообщение" in message.content.lower():
                if message.author.id == 138957703853768705:
                    res = message.content.split('|')
                    channel = res[1]
                    content = res[2]
                    discord_channel = self.get_channel(int(channel))
                    await discord_channel.send(content)
                    return True
                else:
                    await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                    return True
            
            ###                                 ###
            ### ОБЩИЕ КОМАНДЫ                   ###
            ###                                 ###
            
            if message.content.lower() == "виталина, ты умеешь мапать?":
                await message.channel.send(f"О, конечно! Совсем недавно я закончила две свои карты. Можешь оценить? https://cdn.discordapp.com/attachments/1187704983651631174/1188428153299943534/MORGENSHTERN_-_SEL_DEDA.osz https://cdn.discordapp.com/attachments/1187704983651631174/1188428257851363328/Team_Grimoire_-_C18H27NO3.osz")
                return True

            if message.content.lower() == "виталина, голос":
                await message.channel.send(f"Пушистый здряв")
                return True

            if message.content.lower() == "виталина, что ты умеешь?":
                await message.channel.send(f"Привет! Я могу отвечать на вопросы, поддерживать беседу и просто развлекать.")
                return True

            if message.content.lower() == "виталина, у нас новенькие":
                await message.channel.send(f"Привет! Основная информация по тому или иному каналу указана в его шапке! Также не забудь заглянуть в <#882372059928354887> Если у тебя возникли вопросы, не стесняйся задавать их в чатике, а теперь - вперед навстречу ярким эмоциям! <:pepeBusiness:1036987708456845391>")
                return True

            if message.content.lower() == "виталина, ранкни карту":
                await message.channel.send(f"Конечно, отправь карту в мою очередь: https://docs.google.com/forms/d/e/1FAIpQLSdn1i6C44nSaxSQRyEeL3_jvXrxFn-U0hAfxUkTYIudatmiTA/viewform?usp=sf_link")
                return True

            if message.content.lower() == "виталина, скинь свой твиттер":
                await message.channel.send(f"Держи! - https://twitter.com/vitalina2222?s=21&t=z8Z3tXn69AOEOpiRpmFttg")
                return True

            if message.content.lower() == "виталина, скинь смешнявку":
                shrine = selectRandomShrine()
                await message.channel.send(shrine)
                return True

            if message.content.lower() == "виталина, витас":
                photos = selectRandomVitas()
                await message.channel.send(photos)
                return True
            
            ###                                 ###
            ### СЛУЧАЙНЫЕ СОБЫТИЯ               ###
            ###                                 ###

            if random_event == 100:
                await message.channel.send(f"Я устала, за меня ответит <@566961732501635093>.")
                return True
            
            if random_event > 98:
                await message.channel.send(f"Собакам слова не давали.")
                return True
            
            if random_event < 2:
                await message.channel.send(f"Лай для меня, собачка.")
                return True

            if random_event > 75 or vitalina_current_mode == "PASSIVE":
                gif = selectRandomGif()
                await message.channel.send(gif)
                return True

            bot_response = await chatgpt_response(message.content)
            await message.channel.send(bot_response)
            return True

intents = discord.Intents.default()
intents.message_content = True
client = Vitalina(intents=intents)


