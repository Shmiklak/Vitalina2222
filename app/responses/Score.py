import discord
from app.vitalina_utilities.utilities import getRankEmoji
def prepare(Score, Beatmap):
    embed=discord.Embed(color=0xd70f8d)
    embed.set_author(name=f"{Score.beatmapset.title_unicode} [{Score.beatmap.version}] - {Score.beatmap.difficulty_rating} ★", 
                     url=Score.beatmap.url, icon_url=f"https://a.ppy.sh/{Score.user_id}")
    embed.add_field(name="**Grade**", value=getRankEmoji(Score.rank), inline=True)
    embed.add_field(name="**PP**", value=Score.pp, inline=True)
    embed.add_field(name="", value="", inline=False)
    embed.add_field(name="Score", value=f"{round(Score.accuracy * 100, 2)}%")
    embed.add_field(name="Accuracy", value='{:,}'.format(Score.score))
    embed.add_field(name="", value="", inline=False)
    embed.add_field(name="Combo", value=f"{Score.max_combo}x/{Beatmap.max_combo}x")
    embed.add_field(name="300 / 100 / 50 / X", value=f"{Score.statistics.count_300} / {Score.statistics.count_100} / {Score.statistics.count_50} / {Score.statistics.count_miss}")
    embed.set_thumbnail(url=Score.beatmapset.covers.list_2x)
    return embed

