import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('SD2022'))
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'im not gonna say pong faggot btw your ping is {round(client.latency * 1000)}ms')

@client.command()
async def roblox(ctx):
    await ctx.send('roblox is a epic and super fun game that was made in 2006.')

@client.command()
async def epic(ctx):
    await ctx.send('pingu and IdkkPinguhh are epic <@341979169162264578> :sunglasses:')

@client.command()
async def gtausername(ctx):
    await ctx.send('IdkkPinguhhs GTA V Online username is ``idkkpinguhh``')

@client.command()
@commands.has_role('Trial Moderator')
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send('**Done purging.**')

@client.command()
@commands.has_role('Moderator')
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send('**Member has been kicked.**')

@client.command()
@commands.has_role('Moderator')
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send('**Member has been banned.**')

client.run('NzAxODI0NTgwOTg5NDg1MTQ3.Xp3HLg.B4CDEiBqBsVz2ZruYAJOnY4xhxQ')
