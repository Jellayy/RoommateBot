import discord


async def peak_hours_starting(client):
    embed = discord.Embed(
        color=discord.Color.red(),
        title="SRP Peak Hours Starting",
        description="Lower all power usage until 6pm"
    )
    embed.set_footer(text="RoommateBot", icon_url=client.user.avatar_url)
    return embed


async def peak_hours_ending(client):
    embed = discord.Embed(
        color=discord.Color.green(),
        title="SRP Peak Hours Ending",
        description="Resume normal power usage"
    )
    embed.set_footer(text="RoommateBot", icon_url=client.user.avatar_url)
    return embed
