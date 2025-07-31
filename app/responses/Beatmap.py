import discord

def prepare(Beatmap):
    embed=discord.Embed(color=0xd70f8d)
    embed.set_author(name=f"{Beatmap.artist} - {Beatmap.title} (mapped by {Beatmap.creator}) is now ranked!!!", 
                     url=f"https://osu.ppy.sh/beatmapsets/{Beatmap.id}")
    embed.set_thumbnail(url=Beatmap.covers.list_2x)
    return embed