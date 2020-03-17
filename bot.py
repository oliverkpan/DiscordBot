import discord #Import Module
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Jarvis is ready")

client.run('')
