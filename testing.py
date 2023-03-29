# -*- coding: cp1252 -*-

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello! I am the One Ring Discord bot.')

bot.run(TOKEN)


