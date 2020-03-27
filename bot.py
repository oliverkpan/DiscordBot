import discord #Import Module
import random
from discord.ext import commands

jarvis = commands.Bot(command_prefix = '!')

#Bot is ready to go
@jarvis.event
async def on_ready():
    print("Jarvis is ready")

#User has joined server
@jarvis.event
async def on_member_join(member):
    print(f'(member) has joined.')

#User has left server
@jarvis.event
async def on_member_remove(member):
    print(f'(member) has left.')

#Ping Test
@jarvis.command()
async def speed(ctx):
    await ctx.send(f'I am {round(jarvis.latency * 1000)}ms fast')

#8 Ball Feature
@jarvis.command(aliases=['8ball'])
async def eight_ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Nah.',
                 'Ehhhh....maybe.',
                 'Oh no brother.',
                 'I say no.',
                 'Very doubtful.',
                 'Looks good.',
                 'Please try again.',
                 'I really cannot say.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#Clear Messages
@jarvis.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

#Kick Member
@jarvis.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

#Ban Member
@jarvis.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

jarvis.run('')
