import discord
from discord.ext import tasks
import datetime as dt
import embeds
import tokens

client = discord.Client()


@client.event
async def on_ready():
    print(f"Signed in as {client.user}")
    peak_hours.start()


@tasks.loop(minutes=1)
async def peak_hours():
    if dt.datetime.now().weekday() <= 4:
        if dt.time(15) <= dt.datetime.now().time() <= dt.time(15, 1):
            for guild in client.guilds:
                for channel in guild.channels:
                    if str(channel) == 'general':
                        await channel.send(f"{guild.roles[0]}", embed=await embeds.peak_hours_starting(client))
        if dt.time(18) <= dt.datetime.now().time() <= dt.time(18, 1):
            for guild in client.guilds:
                for channel in guild.channels:
                    if str(channel) == 'general':
                        await channel.send(f"{guild.roles[0]}", embed=await embeds.peak_hours_ending(client))

client.run(tokens.discord_token())
