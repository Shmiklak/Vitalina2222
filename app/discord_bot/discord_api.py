from dotenv import load_dotenv
import discord
import os
import random
from app.chatgpt_ai.openai import chatgpt_response
from app.vitalina_utilities.utilities import selectRandomGif, bcolors, selectRandomVitas, selectRandomShrine, selectRandomUser
from app.database.database import dbInsert, selectRandomMessage, saveUser, getUser, signUpUserForGiveaway, truncateGiveaway, selectRandomGiveawayUser
import app.osu.api
import app.responses.User
import app.responses.Score

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')
discord_client = os.getenv('DISCORD_CLIENT_ID')

vitalina_triggers = ['витал', 'vital', '1187685558382772254', 'гуталин', 'буталин', 'оленина']

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

vitalina_current_mode = "NORMAL"

vitalina_ignore_list = []

class Vitalina(discord.Client):
    
    async def on_ready(self):
        await tree.sync()
        await self.change_presence(activity=discord.Game(name="osu!"))
        discord_channel = self.get_channel(int(1216656123239731220))
        await discord_channel.send("Виталина успешно запустилась.")
        return True

    async def on_message(self, message):
        if message.author == self.user or message.author.id in vitalina_ignore_list or message.author.bot:
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

        pizda_event = random.randint(0,2)
    
        if (message.content.lower() == "да" or message.content.lower() == "da") and vitalina_current_mode != "SLEEP" and pizda_event == 1:
            await message.channel.send("https://cdn.discordapp.com/attachments/1204044194499403776/1204394774107525161/wk7pnm_dqkY.png?ex=65d4930a&is=65c21e0a&hm=361e66ff592612704a2aa619b202244a073079dff3c425929f46bf9d7e318703&")
            return True
        
        if (message.content.lower() == "нет" or message.content.lower() == "net") and vitalina_current_mode != "SLEEP" and pizda_event == 1:
            await message.channel.send("Пидора ответ.")
            return True

        if (message.content.lower() == "я" or message.content.lower() == "ya") and vitalina_current_mode != "SLEEP" and pizda_event == 1:
            await message.channel.send("Головка от хуя.")
            return True

        random_event = random.randint(0, 100)
        rare_events = random.randint(0, 1000)
        
        print(bcolors.OKGREEN, "ТЕКУЩАЯ ВЕРОЯТНОСТЬ: ", random_event, bcolors.ENDC)
        print(bcolors.OKGREEN, "ТЕКУЩАЯ РЕДКАЯ ВЕРОЯТНОСТЬ: ", rare_events, bcolors.ENDC)

        if vitalina_current_mode == "AI_ONLY":
            random_event = 50
            rare_events = 0

        if message.author.id == 662608589499924491:
            if random_event == 100:
                await message.channel.send(f"https://tenor.com/view/mother-sgnila-cute-dance-moves-bear-gif-16312770")
                return True


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
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192:
                bot_response = await chatgpt_response("MARVOLLO_HISTORY")
                await message.channel.send(bot_response)
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if message.content.lower() == "виталина, сброс":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192:
                bot_response = await chatgpt_response("MARVOLLO_RESET")
                await message.channel.send(f"Виталина была сброшена с моста.<:pepeBusiness:1036987708456845391>")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
        
        if message.content.lower() == "виталина, обычный режим":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192:
                vitalina_current_mode = "NORMAL"
                await message.channel.send("Изменила режим работы на обычный.")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
        
        if message.content.lower() == "виталина, пассивный режим":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192:
                vitalina_current_mode = "PASSIVE"
                await message.channel.send("Изменила режим работы на пассивный.")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if message.content.lower() == "виталина, агрессивный режим":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192:
                vitalina_current_mode = "AGRESSIVE"
                await message.channel.send("Изменила режим работы на агрессивный.")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if message.content.lower() == "виталина, режим резня":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192:
                vitalina_current_mode = "VERY_AGRESSIVE"
                await message.channel.send("РЕЗНЯ")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if message.content.lower() == "виталина, режим спячка":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192:
                vitalina_current_mode = "SLEEP"
                await message.channel.send("Всем спокойной ночи!")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True

        if message.content.lower() == "виталина, умный режим":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192:
                vitalina_current_mode = "AI_ONLY"
                await message.channel.send("Теперь я знаю всё на этом свете.")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if message.content.lower() == "виталина, русские":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192:
                role = message.guild.get_role(1238609813102006435)
                await message.channel.send("Начинаю чё то делать")
                for member in message.guild.members:
                    member_name = member.display_name

                    if member.nick != None:
                        member_name = member.nick

                    if await app.osu.api.isRussian(member_name):
                        try:
                            await member.add_roles(role)
                            await message.channel.send("Дала роль " + member_name)
                        except:
                            await message.channel.send("Не могу дать роль пользователю " + member_name)
                            continue
                    else:
                        await message.channel.send("Пользователь " + member_name + " не русский либо у него нет аккаунта в osu!")
                        continue
                await message.channel.send("Чё то сделала)")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True


        if message.content.lower() == "настюха, красные мрази":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192:
                
                daddy_role = message.guild.get_role(1339215989849591871)
                expert_role = message.guild.get_role(1339215913924296726)
                master_role = message.guild.get_role(1339215759611662379)
                bro_role = message.guild.get_role(1339215624542621718)

                await message.channel.send("Начинаю чё то делать")
                for member in message.guild.members:
                    member_name = member.display_name

                    if member.nick != None:
                        member_name = member.nick

                    new_user_data = await app.osu.api.isRanked(member_name)

                    if (new_user_data == None):
                        await message.channel.send("не нашла тебя или я сломалась " + member_name)
                        continue
                    if (new_user_data["is_bro"]):
                        await member.add_roles(bro_role)
                        await message.channel.send("ранкед бро " + member_name)
                    if (new_user_data["is_master"]):
                        await member.add_roles(master_role)
                        await message.channel.send("мастер грандмастер " + member_name)
                    if (new_user_data["is_expert"]):
                        await member.add_roles(expert_role)
                        await message.channel.send("эксперт про макс " + member_name)
                    if (new_user_data["is_expert"]):
                        await member.add_roles(daddy_role)
                        await message.channel.send("ТРАХНИ МЕНЯ ПАПОЧКА " + member_name)

                await message.channel.send("начинаем буллить красных")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        ### виталина, отправляем сообщение|CHANNEL_ID|MESSAGE

        if "виталина, отправляем сообщение" in message.content.lower():
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192:
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
        
        if message.content.lower() == "виталина, начинаем раздачу саппортеров на спавне":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 391901940457537538:
                # truncateGiveaway()
                await message.channel.send("We are starting a giveaway of one month of osu! supporter. Please use the button below to sign up.<:pepeBusiness:1036987708456845391>", view=GiveawayButton(timeout=None))
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True

        if message.content.lower() == "виталина, определяем победителя саппортера":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 391901940457537538:
                user_id = selectRandomGiveawayUser()
                await message.channel.send("Hey, <@" + str(user_id) + ">, congratulations! You just won one month of osu! supporter. Please contact nemidnight for details.<:pepeBusiness:1036987708456845391>")
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
            await message.channel.send(f"Привет! Основная информация по тому или иному каналу указана в его шапке! Также не забудь заглянуть в <#882372059928354887>. Если у тебя возникли вопросы, не стесняйся задавать их в чатике, а теперь - вперед навстречу ярким эмоциям! <:pepeBusiness:1036987708456845391>")
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
            
        if rare_events > 960 or (vitalina_current_mode == "VERY_AGRESSIVE" and rare_events > 760):
            # if message.guild.id != 1248156231462424728:
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

            # if message.guild.id == 1248156231462424728:
            #     if random_event > 65 or vitalina_current_mode == "PASSIVE":
            #         gif = selectRandomGif()
            #         await message.channel.send(gif)
            #         return True
            #     bot_response = await chatgpt_response(message.content, True)
            #     await message.channel.send(bot_response)
            #     return True

            if random_event < 15 or vitalina_current_mode == "AGRESSIVE" or vitalina_current_mode == "VERY_AGRESSIVE":
                await message.channel.send(selectRandomMessage())
                return True

            if random_event == 52:
                user = selectRandomUser()
                await message.channel.send(f"Я устала, за меня ответит <@" + user + ">.")
                return True
            
            if random_event == 100:
                await message.channel.send(f"Собакам слова не давали.")
                return True
            
            if random_event < 10:
                await message.channel.send(f"Лай для меня, собачка.")
                return True

            if random_event > 65 or vitalina_current_mode == "PASSIVE":
                gif = selectRandomGif()
                await message.channel.send(gif)
                return True

            bot_response = await chatgpt_response(message.content)
            await message.channel.send(bot_response)
            return True
        
    async def on_member_join(self, member):
        if (member.guild.id == 788166617308987416):
            channel = self.get_channel(788404299784912907)
            await channel.send(f"Hello {member.mention}! Welcome to our server. Please read <#882372059928354887> before you proceed. Once you read it, please use button below to get verified. In case you don't have a valid osu! account or have been restricted please contact Observer Wards to manually verify you.<:pepeBusiness:1036987708456845391>", view=VerificationButton())
        if (member.guild.id == 1248156231462424728):
            channel = self.get_channel(1248172190923362345)
            await channel.send(f"Hello {member.mention}! Welcome to our server. Please use button below to get verified. In case you don't have a valid osu! account or have been restricted please contact server administrators to manually verify you.<:pepeBusiness:1036987708456845391>", view=MangoVerificationButton())
            
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = Vitalina(intents=intents)

tree = discord.app_commands.CommandTree(client)

class VerificationButton(discord.ui.View):
    @discord.ui.button(label="Verify", style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction: discord.Interaction, button):
        await interaction.response.send_modal(VerificationModal())

class VerificationModal(discord.ui.Modal, title='Verification'):
    name = discord.ui.TextInput(
        label='Your osu! profile username',
        placeholder='Please ensure to enter valid osu! name'
    )

    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        user = interaction.user

        new_user_data = await app.osu.api.checkUserRoles(self.name.value)

        if (new_user_data == None):
            await interaction.response.send_message(f'I could not find osu! profile with username {self.name.value}. Please ask observer wards to verify you manually.')
            return False

        verified_role = guild.get_role(788409376598917171)
        russian_role = guild.get_role(1238609813102006435)
        ranked_role = guild.get_role(795277624309055509)

        saveUser(user.id, new_user_data["user"].id)
        await user.add_roles(verified_role)
        await user.edit(nick=self.name.value)
        if (new_user_data["is_russian"]):
            await user.add_roles(russian_role)
        if (new_user_data["is_ranked"]):
            await user.add_roles(ranked_role)

        await interaction.response.send_message(f'You have been verified and your discord account is now linked with {self.name.value} osu! profile.')

    async def on_error(self, interaction: discord.Interaction):
        await interaction.response.send_message('Oops! Something went wrong. Please ask observer wards to verify you manually.')


class MangoVerificationButton(discord.ui.View):
    @discord.ui.button(label="Verify", style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction: discord.Interaction, button):
        await interaction.response.send_modal(MangoVerificationModal())

class MangoVerificationModal(discord.ui.Modal, title='Verification'):
    name = discord.ui.TextInput(
        label='Your osu! profile username',
        placeholder='Please ensure to enter valid osu! name'
    )

    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        user = interaction.user

        new_user_data = await app.osu.api.checkUserRoles(self.name.value)

        if (new_user_data == None):
            await interaction.response.send_message(f'I could not find osu! profile with username {self.name.value}. Please ask server administrators to verify you manually.')
            return False

        verified_role = guild.get_role(1248172223404048466)
        saveUser(user.id, new_user_data["user"].id)
        await user.add_roles(verified_role)
        await user.edit(nick=self.name.value)

        await interaction.response.send_message(f'You have been verified and your discord account is now linked with {self.name.value} osu! profile.')

    async def on_error(self, interaction: discord.Interaction):
        await interaction.response.send_message('Oops! Something went wrong. Please ask server administrators to verify you manually.')

class GiveawayButton(discord.ui.View):
    @discord.ui.button(label="Sign Up", style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction: discord.Interaction, button):
        if (signUpUserForGiveaway(interaction.user.id)):
            await interaction.response.send_message("You have successfully signed up for this giveaway. Please wait for results.", ephemeral=True)
        else:
            await interaction.response.send_message("You cannot sign up for a giveaway multiple times. Please wait for results.", ephemeral=True)

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
    return True

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
