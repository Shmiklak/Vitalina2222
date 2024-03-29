from dotenv import load_dotenv
import discord
import os
import random
from app.chatgpt_ai.openai import chatgpt_response
from app.vitalina_utilities.utilities import selectRandomGif, bcolors, selectRandomVitas, selectRandomShrine, selectRandomUser
from app.database.database import dbInsert, selectRandomMessage, saveUser, getUser
import app.osu.api
import app.responses.User
import app.responses.Score

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')
discord_client = os.getenv('DISCORD_CLIENT_ID')

vitalina_triggers = ['витал', 'vital', '1187685558382772254', 'гуталин', 'буталин']

# if os.getenv("MODE") == "DEV":
    # vitalina_triggers = ['наст', 'nast']

recent_senders = []
recent_messages = []
consecutive_messages = 0
required_consecutive_messages = 3


#
# NORMAL
# PASSIVE
# AGRESSIVE
# VERY_AGRESSIVE
# SLEEP
# AI_ONLY
#

vitalina_current_mode = "AI_ONLY"

vitalina_ignore_list = []

class Vitalina(discord.Client):
    
    async def on_ready(self):
        await tree.sync()
        await self.change_presence(activity=discord.Game(name="osu!"))
        discord_channel = self.get_channel(int(1216656123239731220))
        await discord_channel.send("Виталина успешно запустилась.")
        return True

    async def on_message(self, message):
        if message.author == self.user or message.author.id in vitalina_ignore_list:
            return False
        
        if isinstance(message.channel, discord.DMChannel):
            await message.channel.send(f"Я не буду отвечать вам в личных сообщениях. Ищите меня на серверах")
            return True

        if message.content == "шмик":
            await message.channel.send(f"Сегодня я вместо него. Чем могу помочь? <:pepeBusiness:1036987708456845391>")
            return True
        
        if message.content != "":
            dbInsert("INSERT INTO all_messages (message) VALUES (%s)", [message.content])
        
        global consecutive_messages
        global recent_senders
        global recent_messages
        global vitalina_current_mode
        global vitalina_triggers

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
    
        if (message.content.lower() == "да" or message.content.lower() == "da") and vitalina_current_mode != "SLEEP":
            await message.channel.send("https://cdn.discordapp.com/attachments/1204044194499403776/1204394774107525161/wk7pnm_dqkY.png?ex=65d4930a&is=65c21e0a&hm=361e66ff592612704a2aa619b202244a073079dff3c425929f46bf9d7e318703&")
            return True
        
        if (message.content.lower() == "нет" or message.content.lower() == "net") and vitalina_current_mode != "SLEEP":
            await message.channel.send("Пидора ответ.")
            return True

        random_event = random.randint(0, 100)
        rare_events = random.randint(0, 1000)
        print(bcolors.OKGREEN, "ТЕКУЩАЯ ВЕРОЯТНОСТЬ: ", random_event, bcolors.ENDC)
        print(bcolors.OKGREEN, "ТЕКУЩАЯ РЕДКАЯ ВЕРОЯТНОСТЬ: ", rare_events, bcolors.ENDC)

        if vitalina_current_mode == "AI_ONLY":
            random_event = 50
            rare_events = 0

        # if message.author.id == 305361927415136258 or message.author.id == 313751415061479426:
        #     if random_event > 95:
        #         await message.channel.send(f"https://tenor.com/view/mother-sgnila-cute-dance-moves-bear-gif-16312770")
        #         return True


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
            if message.author.id == 138957703853768705 or message.author.id == 395117543406436353 or message.author.id == 143343954816008192:
                bot_response = await chatgpt_response("MARVOLLO_HISTORY")
                await message.channel.send(bot_response)
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if message.content.lower() == "виталина, сброс":
            if message.author.id == 138957703853768705 or message.author.id == 395117543406436353 or message.author.id == 143343954816008192:
                bot_response = await chatgpt_response("MARVOLLO_RESET")
                await message.channel.send(f"Виталина была сброшена с моста.<:pepeBusiness:1036987708456845391>")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
        
        if message.content.lower() == "виталина, обычный режим":
            if message.author.id == 138957703853768705 or message.author.id == 395117543406436353 or message.author.id == 143343954816008192:
                vitalina_current_mode = "NORMAL"
                await message.channel.send("Изменила режим работы на обычный.")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
        
        if message.content.lower() == "виталина, пассивный режим":
            if message.author.id == 138957703853768705 or message.author.id == 395117543406436353 or message.author.id == 143343954816008192:
                vitalina_current_mode = "PASSIVE"
                await message.channel.send("Изменила режим работы на пассивный.")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if message.content.lower() == "виталина, агрессивный режим":
            if message.author.id == 138957703853768705 or message.author.id == 395117543406436353 or message.author.id == 143343954816008192:
                vitalina_current_mode = "AGRESSIVE"
                await message.channel.send("Изменила режим работы на агрессивный.")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if message.content.lower() == "виталина, режим резня":
            if message.author.id == 138957703853768705 or message.author.id == 395117543406436353 or message.author.id == 143343954816008192:
                vitalina_current_mode = "VERY_AGRESSIVE"
                await message.channel.send("РЕЗНЯ")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if message.content.lower() == "виталина, режим спячка":
            if message.author.id == 138957703853768705 or message.author.id == 395117543406436353 or message.author.id == 143343954816008192:
                vitalina_current_mode = "SLEEP"
                await message.channel.send("Всем спокойной ночи!")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if message.content.lower() == "виталина, умный режим":
            if message.author.id == 138957703853768705 or message.author.id == 395117543406436353 or message.author.id == 143343954816008192:
                vitalina_current_mode = "AI_ONLY"
                await message.channel.send("Теперь я знаю всё на этом свете.")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
        
        ### виталина, отправляем сообщение|CHANNEL_ID|MESSAGE

        if "виталина, отправляем сообщение" in message.content.lower():
            if message.author.id == 138957703853768705 or message.author.id == 395117543406436353 or message.author.id == 143343954816008192:
                res = message.content.split('|')
                channel = res[1]
                content = res[2]
                discord_channel = self.get_channel(int(channel))
                await discord_channel.send(content)
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if vitalina_current_mode == "SLEEP":
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
            await message.channel.send(f"Привет! Основная информация по тому или иному каналу указана в его шапке! Также не забудь заглянуть в <#882372059928354887>. Также не забудь заглянуть в <#882372059928354887> Если у тебя возникли вопросы, не стесняйся задавать их в чатике, а теперь - вперед навстречу ярким эмоциям! <:pepeBusiness:1036987708456845391>")
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
            
        if rare_events > 880 or (vitalina_current_mode == "VERY_AGRESSIVE" and rare_events > 660):
            await message.channel.send(selectRandomMessage())
            return True

        if '1187685558382772254' in message.content:
            if random_event > 80:
                await message.channel.send(f"https://tenor.com/view/chungus-pinged-ben-shapiro-discord-big-gif-21424212")
                return True 
        
        trigger_vitalina = False

        for text in vitalina_triggers:
            if text in message.content.lower():
                trigger_vitalina = True

        if message.type == discord.MessageType.reply:
            reference = await message.channel.fetch_message(message.reference.message_id)

            if reference.author.id == self.user.id:
                trigger_vitalina = True


        if trigger_vitalina:           
            ###                                 ###
            ### СЛУЧАЙНЫЕ СОБЫТИЯ               ###
            ###                                 ###

            if random_event < 25 or vitalina_current_mode == "AGRESSIVE" or vitalina_current_mode == "VERY_AGRESSIVE":
                await message.channel.send(selectRandomMessage())
                return True

            # if random_event == 100:
            #     user = selectRandomUser()
            #     await message.channel.send(f"Я устала, за меня ответит <@" + user + ">.")
            #     return True
            
            if random_event == 100:
                await message.channel.send(f"Собакам слова не давали.")
                return True
            
            if random_event < 5:
                await message.channel.send(f"Лай для меня, собачка.")
                return True

            if random_event > 75 or vitalina_current_mode == "PASSIVE":
                gif = selectRandomGif()
                await message.channel.send(gif)
                return True

            bot_response = await chatgpt_response(message.content)
            await message.channel.send(bot_response)
            return True
        
    async def on_member_join(self, member):
        channel = self.get_channel(788404299784912907)
        await channel.send(f"Hello {member.mention}! Welcome to our server. Please read <#882372059928354887> before you proceed. Once you read it, send your osu! profile link so <@&937077604203262023> can verify you.<:pepeBusiness:1036987708456845391>")

        

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = Vitalina(intents=intents)

tree = discord.app_commands.CommandTree(client)

@tree.command(name = "osu_user", description = "Get osu! profile information. Available modes are osu, catch, taiko, mania")
async def self(interaction: discord.Interaction, name: str="", mode: str=""):

    query = name
    
    if query == "":
        user_id = getUser(interaction.user.id)

        if user_id == "ERROR":
            await interaction.response.send_message("You don't have an osu! profile assigned to your Discord account, neither provided username. Please set your own profile using /osu_set_profile")
            return False

        query = user_id

    user = await app.osu.api.getOsuUser(query, mode)
    await interaction.response.defer()
    await interaction.followup.send(embed=app.responses.User.prepare(user))

@tree.command(name = "osu_set_profile", description = "Assings the given osu! profile to your Discord account")
async def self(interaction: discord.Interaction, name: str):
    user = await app.osu.api.getOsuUser(name)
    saveUser(interaction.user.id, user.id)
    await interaction.response.defer()
    await interaction.followup.send(f"Your Discord account is now connected with your osu! profile {user.username}")

@tree.command(name = "osu_recent_score", description = "Get information about your latest score")
async def self(interaction: discord.Interaction):

    user_id = getUser(interaction.user.id)
    if user_id == "ERROR":
        await interaction.response.send_message("You don't have an osu! profile assigned to your Discord account, neither provided username. Please set your own profile using /osu_set_profile")
        return False
    score = await app.osu.api.getRecentScore(user_id)

    if not score:
        await interaction.response.send_message("You don't have recent scores to display.")
        return False

    beatmap = await app.osu.api.getBeatmap(score[0].beatmap.id)
    await interaction.response.defer()
    await interaction.followup.send(f"**Recent play for {score[0]._user.username}**", embed=app.responses.Score.prepare(score[0], beatmap))
