import discord
from discord.ext import commands

class Test(commands.Cog):

    def __init__(self, jarvis):
        self.jarvis = jarvis

    @commands.command()
    async def test(self, ctx):
        await ctx.send('test')

def setup(jarvis):
    jarvis.add_cog(Test(jarvis))
