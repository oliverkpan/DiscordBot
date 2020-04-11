import discord #Import Module
import os
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
    await ctx.send(f'Kicked {member.mention}')

#Ban Member
@jarvis.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

#Unban Member
@jarvis.command()
async def unban(ctx, *, member):
    banned = await ctx.guild.bans() #list of banned entry in server
    member_name, member_discriminator = member.split('#')

    for entry in banned:
        user = entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return

#cogs Load
@jarvis.command()
async def load(ctx, extension): #Extension is COG
    jarvis.load_extension(f'cogs.{extension}')

#cogs Unload
@jarvis.command()
async def unload(ctx, extension): #Extension is COG
    jarvis.unload_extension(f'cogs.{extension}')

#cogs Reload
@jarvis.command()
async def reload(ctx, extension):
    jarvis.unload_extension(f'cogs.{extension}')
    jarvis.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        jarvis.load_extension(f'cogs.{filename[:-3]}') #cut .py

jarvis.run('')
