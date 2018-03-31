import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():  
    print ("0 Errors found so far.")
    print ("Starting up... " + bot.user.name)
        
@bot.command(pass_context=True)
async def cmds(ctx):
    emb_name = discord.Embed(title="Moderation Commands.", description="***.cmds*** | Brings up this message!\n***.info [user]*** | Brings up infomation about a user!\n***.kick [user]*** | Kicks the specified user!", color=discord.Color.green())
    await bot.send_message(ctx.message.channel, embed=emb_name)
    emb_name = discord.Embed(title="User Commands.", description="***.afk*** | Makes you AFK!\n***.unafk*** | Removes your AFK!\n***.support*** | Links you to our support server!", color=discord.Color.green())
    await bot.send_message(ctx.message.channel, embed=emb_name)
    emb_name = discord.Embed(title="Fun Commands.", description="***.birthday*** | Whos birthday is it??\n***.backflip*** | Flip it!", color=discord.Color.green())
    await bot.send_message(ctx.message.channel, embed=emb_name)
    

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("Name: {}".format(user.name))
    await bot.say("ID: {}".format(user.id))
    await bot.say("Status: {}".format(user.status))
    print ("Info sent.")

@bot.command(pass_context=True)
async def afk(ctx):
    await bot.say(f"@{ctx.message.author} is now ***AFK*** !")

@bot.command(pass_context=True)
async def unafk(ctx):
    await bot.say(f"@{ctx.message.author} is no longer ***AFK*** !")

@bot.command(pass_context=True)
async def support(ctx):
    await bot.say("Join our support server! https://discord.gg/cNXwKmw")

@bot.command(pass_context=True)
async def birthday(ctx):
    emb_name = discord.Embed(title=":tada: Happy birthday! :tada:", description="Happy Birthday to You\nHappy Birthday to You\nHappy Birthday Dear Discord User\nHappy Birthday to You", color=discord.Color.green())
    await bot.send_message(ctx.message.channel, embed=emb_name)

@bot.command(pass_context=True)
async def backflip(ctx):
    await bot.say(f"@{ctx.message.author} did a backflip! but he broke his neck...")

@bot.command(pass_context = True)
async def kick(ctx, userName: discord.User):
 if "Admin" in [role.name for role in ctx.message.author.roles]:
     await bot.kick(userName)
     await bot.say (f"@{ctx.message.author} has kicked a person!")
 else:
            await bot.say ("You do not have permission to use this command! You need to have the 'admin' rank!")

@bot.command(pass_context = True)
async def mute(ctx, userName: discord.User):
 if "Admin" in [role.name for role in ctx.message.author.roles]:
      overwrite = discord.PermissionOverwrite().send_messages=False
      bot.edit_channel_permissions(ctx.message.channel,userName,overwrite)
      await bot.say ("Output")
 else:
            await bot.say ("You do not have permission to use this command! You need to have the 'admin' rank!")


bot.run("NDI5NzE0NTUwMjI5Njk2NTIy.DaFqyg.rraiZ8t4N730zIs1RjIZg-xy1vQ")
