import discord
from discord.ext import commands

class Command(commands.Cog):

    def __init__(self, jarvis):
        self.jarvis = jarvis
