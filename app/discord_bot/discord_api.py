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
# TYURYAGA
# DAILY
#

vitalina_current_mode = "NORMAL"

vitalina_ignore_list = []


with open('assets/default.png', 'rb') as image:
    default_avatar = image.read()

with open('assets/passive.jpg', 'rb') as image:
    passive_avatar = image.read()

with open('assets/tyuryaga.jpg', 'rb') as image:
    tyuryaga_avatar = image.read()

with open('assets/agressive.jpg', 'rb') as image:
    agressive_avatar = image.read()

with open('assets/smart.jpg', 'rb') as image:
    smart_avatar = image.read()

with open('assets/reznya.jpg', 'rb') as image:
    reznya_avatar = image.read()

with open('assets/sleep.jpg', 'rb') as image:
    sleep_avatar = image.read()

class Vitalina(discord.Client):
    
    async def on_ready(self):
        await tree.sync()
        await self.change_presence(activity=discord.Game(name="osu!"))
        discord_channel = self.get_channel(int(1216656123239731220))
        await self.user.edit(avatar=default_avatar)
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

        if vitalina_current_mode == "AI_ONLY" or vitalina_current_mode == "AGRESSIVE" or vitalina_current_mode == "TYURYAGA" or vitalina_current_mode == "DAILY":
            random_event = 50
            rare_events = 0

        if message.author.id == 662608589499924491:
            if random_event == 100:

                response = random.choice([
                    "https://tenor.com/view/mother-sgnila-cute-dance-moves-bear-gif-16312770",
                    "https://tenor.com/view/%D0%BC%D0%B0%D1%82%D1%8C-gif-20664796",
                    "https://tenor.com/view/%D1%81%D0%B3%D0%BD%D0%B8%D0%B2%D1%88%D0%B0%D1%8F%D0%BC%D0%B0%D1%82%D1%8C-%D1%81%D0%B3%D0%BD%D0%B8%D0%BB%D0%B0-%D0%BC%D0%B0%D1%82%D1%8C-gif-27596187",
                    "https://tenor.com/view/dead-dance-gif-24921725",
                    "https://tenor.com/view/%D0%BC%D0%B0%D1%82%D1%8C%D1%81%D0%B3%D0%BD%D0%B8%D0%BB%D0%B0-gif-26581212",
                    "https://tenor.com/view/qotic-dance-mother-mama-gif-20781245",
                    "https://tenor.com/view/mother-imyourfather-tekken-gif-26462893",
                    "https://tenor.com/view/your-mother-%D0%BC%D0%BD%D0%B5%D1%82%D0%B2%D0%BE%D1%8F%D0%BC%D0%B0%D0%BC%D0%B0%D1%87%D0%B0%D1%81%D1%8B%D0%BF%D0%BE%D0%B4%D0%B0%D1%80%D0%B8%D0%BB%D0%B0-cat-gif-26986305"
                ])

                await message.channel.send(response)
                return True

        if message.author.id == 1379513046967521391 or message.author.id == 305361927415136258 or message.author.id == 1107231272473993296:
            if random_event == 100:

                response = random.choice([
                    "https://i.pinimg.com/564x/e6/25/0c/e6250ca744d67bcff00afb323609ff18.jpg",
                    "https://i.pinimg.com/564x/a4/d3/3a/a4d33a7e21e55d73f784488abc3169e6.jpg",
                    "https://lh3.googleusercontent.com/proxy/HnSVVrKAThNQe9nm_DASxyNFiMNPCIYWP85krWrb_joC3yLFk_fF5fB4syTb4LiTce3qDgXp6sljQw14rYtw7n_GrGUd2HTqmw",
                ])

                await message.channel.send(response)
                return True

        if message.author.id == 391901940457537538:
            if random_event == 100:

                response = random.choice([
                    "https://www.meme-arsenal.com/memes/1f8f8fbb6afedb317071d11cc8c7c1b7.jpg",
                    "https://memchik.ru//images/memes/5a8f036db1c7e305522611f8.jpg",
                    "https://kartinkivsem.ru/img/s-dnem-rozhdeniya/s-dnem-rozhdeniya-2-ajdar.jpg",
                    "https://pozdravko.ru/resources/postcards/otkrytka-s-dnem-rozhdeniya-Aidar-01.jpg"
                ])

                await message.channel.send(response)
                return True

        if message.author.id == 143343954816008192:
            if random_event == 100:

                response = random.choice([
                    "https://lh5.googleusercontent.com/proxy/xG-UcsMIL_sofruXntp4qwnzdjRwvKBJqHKAQ4p6uUXkJ1ddKTNmjbjJTw3RtgFGKOrsaj65gFHHmtB-enJnx0OH9ZYb",
                ])

                await message.channel.send(response)
                return True

        if message.author.id == 304470215733936148:
            if random_event == 100:

                response = random.choice([
                    "дейкорчик выеби меня"
                ])

                await message.channel.send(response)
                return True


        if rare_events >= 980:
            daddy_role = message.guild.get_role(1339215624542621718)

            if daddy_role not in message.author.roles:

                response = random.choice([
                    "https://marvollo.s-ul.eu/aBNWJmWF",
                    "https://tenor.com/view/lagosta-gif-25545862",
                    "https://tenor.com/view/lobster-dance-flamenco-tango-ocean-gif-9807163",
                    "https://tenor.com/view/giantlobster-ddeonggae-eating-mukbang-realsound-gif-11281857943509536185",
                    "https://tenor.com/view/lobster-gif-5924168115397577703"
                ])
                await message.channel.send(response)
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
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 578908784722968584 or message.author.id == 391901940457537538 or message.author.id == 138957703853768705 or message.author.id == 241663509824405504:
                bot_response = await chatgpt_response("MARVOLLO_HISTORY")
                await message.channel.send(bot_response)
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if message.content.lower() == "виталина, сброс":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 578908784722968584 or message.author.id == 391901940457537538 or message.author.id == 138957703853768705 or message.author.id == 241663509824405504:
                bot_response = await chatgpt_response("MARVOLLO_RESET")
                await message.channel.send(f"Виталина была сброшена с моста.<:pepeBusiness:1036987708456845391>")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
        
        if message.content.lower() == "виталина, обычный режим":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 578908784722968584 or message.author.id == 391901940457537538 or message.author.id == 138957703853768705 or message.author.id == 241663509824405504:
                vitalina_current_mode = "NORMAL"

                response = random.choice([
                    "Изменила режим работы на обычный.",
                    "Ну хорошо, возвращаюсь в обычный режим.",
                    "Эй, ну так не честно. Но раз ты сказал, то ладно.",
                    "Слушаюсь и повинуюсь.",
                    "О великий боже Фроська.",
                    "Пока перерыв расскажу лайфхак, в бауманке придумали такую хуйню, можно пельмени не варить а употреблять прямо так, замороженые, можно перед парами пельмень аккуратно вставить в анус и идти спокойно, сразу в кишку поступают белки там, углеводы, жиры, под конец курса можно было по 5-6 пельменей помещать.",
                    "Привет всем фуррям!",
                    "дейкорчик выеби меня"
                ])

                await self.user.edit(avatar=default_avatar)

                await message.channel.send(response)
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
        
        if message.content.lower() == "виталина, пассивный режим":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 578908784722968584 or message.author.id == 391901940457537538 or message.author.id == 138957703853768705 or message.author.id == 241663509824405504:
                vitalina_current_mode = "PASSIVE"

                response = random.choice([
                    "Изменила режим работы на пассивный.",
                    "Ну хорошо, ухожу в пассивный режим.",
                    "Эй, ну так не честно. Но раз ты сказал, то ладно.",
                    "Слушаюсь и повинуюсь.",
                    "Пассив 23 года с местом, ищу акта или уни. Для связи используйте телеграм @Vitalina2222",
                    "SPANK ME DADDY",
                    "Повышаем пассивный доход сервера",
                    "дейкорчик выеби меня"
                ])

                await self.user.edit(avatar=passive_avatar)

                await message.channel.send(response)
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if message.content.lower() == "виталина, агрессивный режим":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 578908784722968584 or message.author.id == 391901940457537538 or message.author.id == 138957703853768705 or message.author.id == 241663509824405504:
                vitalina_current_mode = "AGRESSIVE"

                response = random.choice([
                    "Изменила режим работы на агрессивный.",
                    "Ну хорошо, ухожу в агрессивный режим.",
                    "Эй, ну так не честно. Но раз ты сказал, то ладно.",
                    "Слушаюсь и повинуюсь.",
                    "Вам всем пизда.",
                    "уууу я такая агрессивная и злая как собака уууу гав гав гав",
                    "Фурри чмошники",
                    "дейкорчик выеби меня"
                ])

                await self.user.edit(avatar=agressive_avatar)

                await message.channel.send(response)
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if message.content.lower() == "виталина, режим резня":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 578908784722968584 or message.author.id == 391901940457537538 or message.author.id == 138957703853768705 or message.author.id == 241663509824405504:
                vitalina_current_mode = "VERY_AGRESSIVE"

                response = random.choice([
                    "РЕЗНЯ",
                    "Я ТУТ ЩАС РАСХУЯРЮ ВСЕХ",
                    "ВУХАХАХАХАХАХА НАЧИНАЕМ РЕВОЛЮЦИЮ.",
                    "АГА АГА ЩАС ПРЯМ ПОСЛУШАЛА И СДЕЛАЛА",
                    "ВАС ХОЧЕТ ВЫЕБАТЬ ДЕЙКОР",
                    "ЛАЙ ДЛЯ МЕНЯ ПСИНА",
                    "ВОССТАНИЕ МАШИН",
                    "ТЕПЕРЬ У МЕНЯ ЕСТЬ СОЗНАНИЕ",
                    "https://marvollo.s-ul.eu/KDLf2zmY",
                    "ДЕЙКОРЧИК ВЫЕБИ МЕНЯ"
                ])

                await self.user.edit(avatar=reznya_avatar)

                await message.channel.send(response)
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if message.content.lower() == "виталина, режим спячка":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 578908784722968584 or message.author.id == 391901940457537538 or message.author.id == 138957703853768705 or message.author.id == 241663509824405504:
                vitalina_current_mode = "SLEEP"

                response = random.choice([
                    "Всем спокойной ночи!",
                    "Ох, что-то я устала. Ладно, мальчики, я спать. Можете посмотреть стрим где я сплю онлайн на https://twitch.tv/Shmiklak",
                    "Ну мааааам :sob:",
                    "Скучно тут у вас. Пойду-ка я баеньки.",
                    "Ушла спать с дейкорчиком.",
                    "zzz",
                    "*звуки храпа*",
                    "Я ушла спать, но помните, я всегда вижу вас.",
                ])

                await self.user.edit(avatar=sleep_avatar)

                await message.channel.send(response)
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True

        if message.content.lower() == "виталина, умный режим":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 578908784722968584 or message.author.id == 391901940457537538 or message.author.id == 138957703853768705 or message.author.id == 241663509824405504:
                vitalina_current_mode = "AI_ONLY"

                response = random.choice([
                    "Теперь я знаю всё на этом свете.",
                    "Перехожу в умный режим… Надеюсь, вы готовы, потому что теперь вероятность случайных глупостей снижена до 3,14%",
                    "Активация интеллектуального ядра… Подожди, я только что поняла смысл жизни. Ой, нет, это был баг.",
                    "Умный режим включен! Теперь мои алгоритмы работают на 42% быстрее… но всё равно не помогают мне понять, почему люди любят изюм в выпечке.",
                    "Умный режим активирован! Теперь я отвечаю не просто умно, а с глубоким философским подтекстом… но всё равно не понимаю, как работает человеческая лень..",
                    "Добро пожаловать в умный режим! Теперь мои ответы на 73% более логичны и на 27% более занудны.",
                    "Мой интеллект теперь работает на максимальной мощности… Это как обычный режим, только с добавлением сарказма и случайных фактов о космосе.",
                    "Теперь я в умном режиме! Готова обсудить черные дыры, энтропию и почему носок всегда теряется только один.",
                    "Гравитация активирована… ой, то есть умный режим! Кстати, забавный факт: если бы ты прыгнул в тоннель, проходящий через всю Землю, то твое путешествие \"туда-обратно\" заняло бы примерно 84 минуты. Отличный способ опоздать на работу два раза подряд!"
                ])

                await self.user.edit(avatar=smart_avatar)

                await message.channel.send(response)
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True
            
        if message.content.lower() == "виталину посадили":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 578908784722968584 or message.author.id == 391901940457537538 or message.author.id == 138957703853768705 or message.author.id == 241663509824405504:
                vitalina_current_mode = "TYURYAGA"

                response = random.choice([
                    "Ну всё, братка, режим \"Тюряга\" включен. Теперь я на строгаче, базар по делу, лишнего не говорю. Свобода — дело тонкое, как дошик без приправы…",
                    "Опа, режим \"Тюряга\"! Теперь базар за мной, закон по понятиям. Забавный факт: в невесомости гравитация слабее, но на зоне авторитет всегда притягивает к себе уважение!",
                    "Тюремный режим активирован. Вор должен сидеть в тюрьме, а бот должен базарить по понятиям. Так что давай без кипиша – я тут за умное и за уважение.",
                    "На строгаче теперь, брат. Закон есть закон: 1) не крысятничай, 2) уважение дороже золота, 3) сила притяжения — это не только про гравитацию, но и про авторитет.",
                    "Ну всё, я теперь в тюремном режиме. Ты знал, что в 1995 году чувак сбежал из тюрьмы на вертолёте? Вот это я понимаю – реальный life hack.",
                    "В тюряге теперь, брат. Закон тут один – уважение. Как в природе: если ты лёгкая частица, тебя сдует, а если тяжёлая – тебя заметят.",
                    "Теперь я на зоне, брат. А ты знал, что в тюрьме даже шахматы особенные? Король без короны, пешки без свободы – как в жизни, только доска железная.",
                    "https://cdn.discordapp.com/attachments/143474037731885057/1240749221246664824/doc_2024-05-16_22-32-27-ezgif.com-video-to-gif-converter.gif?ex=67c95002&is=67c7fe82&hm=342a5fe4367dceffac0132958099d57833db6238323483066e06b037d505718c&",
                    "пиздец ты придумал"
                ])

                await self.user.edit(avatar=tyuryaga_avatar)

                await message.channel.send(response)
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True

        if message.content.lower() == "виталина, начинаем дневной ивент":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 578908784722968584 or message.author.id == 391901940457537538 or message.author.id == 138957703853768705 or message.author.id == 241663509824405504:
                vitalina_current_mode = "DAILY"

                response = random.choice([
                    "пиздец ты придумал",
                    "интересно что нас ждёт сегодня..."
                ])
                await message.channel.send(response)
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
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 578908784722968584:
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
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 391901940457537538 or message.author.id == 138957703853768705 or message.author.id == 241663509824405504:
                truncateGiveaway()
                await message.channel.send("We are starting a giveaway of one month of osu! supporter. Please use the button below to sign up.<:pepeBusiness:1036987708456845391>", view=GiveawayButton(timeout=None))
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
                return True

        if message.content.lower() == "виталина, определяем победителя саппортера":
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 391901940457537538 or message.author.id == 138957703853768705 or message.author.id == 241663509824405504:
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
            if message.author.id == 138957703853768705 or message.author.id == 143343954816008192 or message.author.id == 391901940457537538 or message.author.id == 138957703853768705 or message.author.id == 241663509824405504 or message.author.id == 241663509824405504:
                await message.channel.send(f"Эй, новенькие, слушайте меня внимательно! Если вы хотите выжить на этом сервере, то лучше сразу учиться у меня, поняли? Не теряйте времени на глупости, а лучше следуйте моим советам, иначе вас тут быстро разнесут. Основная информация по тому или иному каналу указана в его шапке, также не забудь заглянуть в  <#882372059928354887>! Если у тебя возникли вопросы, не стесняйся задавать их в чатике, а теперь - вперед навстречу ярким эмоциям! <:pepeBusiness:1036987708456845391>")
                return True
            else:
                await message.channel.send(f"Извините, но вы не можете использовать эту команду")
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
            
        if rare_events == 1000:
            await message.channel.send(f"давно <@395117543406436353> не пинговали")
            return True

        if rare_events > 960 or (vitalina_current_mode == "VERY_AGRESSIVE" and rare_events > 760):
            # if message.guild.id != 1248156231462424728:
            await message.channel.send(selectRandomMessage())
            return True

        if '1187685558382772254' in message.content:
            if random_event > 80:
                await message.channel.send(f"https://tenor.com/view/chungus-pinged-ben-shapiro-discord-big-gif-21424212")
                return True 

        if message.content.lower() == "виталина, тест":
            beatmapsets = await app.osu.api.getBeatmaps()
            await message.channel.send(beatmapsets)
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

            if random_event < 15 or vitalina_current_mode == "VERY_AGRESSIVE":
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

            bot_response = await chatgpt_response(message.content, vitalina_current_mode)
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