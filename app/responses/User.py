import discord

def prepare(User):
    embed=discord.Embed(title=User.username, url=User.avatar_url, description=User.title, color=0xd70f8d)
    embed.set_thumbnail(url=f"https://a.ppy.sh/{User.id}")
    embed.add_field(name="Performance Points", value=User.statistics.pp, inline=True)
    embed.add_field(name="Rank", value=f"#{User.statistics.global_rank}", inline=True)
    embed.add_field(name="", value="", inline=False)
    embed.add_field(name="Country", value=User.country_code, inline=True)
    embed.add_field(name="Country rank", value=f"#{User.statistics.country_rank}", inline=True)
    embed.set_footer(text=f"https://osu.ppy.sh/u/{User.id}")
    return embed