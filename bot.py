import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import youtube_dl
  
bot = commands.Bot(command_prefix='.')
  
@bot.event
async def on_ready():  
    print ("0 Errors found so far.")
    print ("DexxedBot is online")
    await bot.change_presence(game=discord.Game(name='Do ".cmds" to get started!'))
          
@bot.command(pass_context=True)
async def cmds(ctx):
    emb_name = discord.Embed(title="Moderation Commands.", description="***.kick [user]*** | Kicks the specified user!\n***.ban [user]*** | Bans the specified user!\n***.clear [amount]*** | Clears the requested amount of messages!", color=discord.Color.green())
    await bot.send_message(ctx.message.channel, embed=emb_name)
    emb_name = discord.Embed(title="User Commands.", description="***.cmds*** | Brings up this message!\n***.afk*** | Makes you AFK!\n***.unafk*** | Removes your AFK!\n***.ping*** | Pong! Checks the bots ping.", color=discord.Color.green())
    await bot.send_message(ctx.message.channel, embed=emb_name)
    emb_name = discord.Embed(title="Social Media.", description="***.twitch*** | Shows you my twitch!\n***.youtube*** | Shows you my youtube!\n***.twitter*** | Shows you my twitter!\n***.instagram*** | Shows you my instagram!", color=discord.Color.green())
    await bot.send_message(ctx.message.channel, embed=emb_name)

 
@bot.command(pass_context = True)
async def kick(ctx, userName: discord.User):
 if "Chat Moderator" in [role.name for role in ctx.message.author.roles]:
     await bot.kick(userName)
     await bot.say(f"@{ctx.message.author} has kicked {userName}!")
 else:
            await bot.say ("You do not have permission to use this command! You need to have the 'chat moderator' rank!")

@bot.command(pass_context = True)
async def ban(ctx, userName: discord.User):
 if "Chat Moderator" in [role.name for role in ctx.message.author.roles]:
     await bot.ban(userName)
     await bot.say(f"@{ctx.message.author} has banned {userName}!")
 else:
            await bot.say ("You do not have permission to use this command! You need to have the 'chat moderator' rank!")
  

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    if "Chat Moderator" in [role.name for role in ctx.message.author.roles]:
        channel = ctx.message.channel
        messages = []
        async for message in bot.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
        await bot.delete_messages(messages)
        await bot.say(f'I have just cleared {amount} messages for you! :smiley:')
    else:
            await bot.say ("You do not have permission to use this command! You need to have the 'chat moderator' rank!")

@bot.command(pass_context=True)
async def ping(ctx):
    t = await bot.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await bot.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))

afkList = []

@bot.command(pass_context=True)
async def afk(ctx):
    afkList.append(ctx.message.author.id)
    await bot.say(f"{ctx.message.author} is now afk!")
 
@bot.command(pass_context=True)
async def unafk(ctx):
    afkList.remove(ctx.message.author.id)
    await bot.say(f"{ctx.message.author} is no longer afk!")


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    for mention in message.mentions:
        if mention.id in afkList:
            await bot.send_message(message.channel, "That user is afk!")

@bot.command(pass_context=True)
async def on_message(message):
        if ctx.message.author.id in afkList:
            afkList.remove(ctx.message.author.id)
            await bot.say("You are no longer afk!")

@bot.command(pass_context=True)
async def twitch(ctx):
    await bot.say('Follow DoubleDexxed on twitch! https://www.twitch.tv/doubledexxed')

@bot.command(pass_context=True)
async def youtube(ctx):
    await bot.say('Subscribe to DoubleDexxed on youtube! https://www.youtube.com/channel/UC0iO3qM9F5D8BHoPuY17zeA?view_as=subscriber')

@bot.command(pass_context=True)
async def twitter(ctx):
    await bot.say('Follow DoubleDexxed on twitter! https://twitter.com/DoubleDexxed')

@bot.command(pass_context=True)
async def instagram(ctx):
    await bot.say('Follow DoubleDexxed on Instagram! https://www.instagram.com/doubledexxed/')

            
bot.run("NTY0OTQwOTQwNDM1OTE0NzU0.XKvMnQ.fp2notG9qPE9nChoDbAYXqwjiBE")
