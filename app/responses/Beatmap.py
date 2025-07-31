import discord

def prepare(Beatmap):
    embed=discord.Embed(color=0xd70f8d, title=f"{Beatmap.artist} - {Beatmap.title} (mapped by {Beatmap.creator}) is now ranked!!!", url=f"https://osu.ppy.sh/beatmapsets/{Beatmap.id}")
    embed.set_author(name=Beatmap.creator, icon_url=f"https://a.ppy.sh/{Beatmap.user_id}")
    embed.set_thumbnail(url=Beatmap.covers.list_2x)
    embed.set_footer(text=f"a new map by our member just got ranked!!")
    return embed