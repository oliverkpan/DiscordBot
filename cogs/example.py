import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, jarvis):
        self.jarvis = jarvis

    @commands.Cog.listener()
    async def on_ready(self):
        print('Jarvis is online')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

def setup(jarvis):
    jarvis.add_cog(Example(jarvis))
