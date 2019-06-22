import discord
import random 
import os
from discord.ext import commands


client = commands.Bot(command_prefix = ".")

@client.event
async def on_member_join(member):
        role = discord.utils.get(member.guild.roles, name="Statis Army")
        await member.add_roles(role)   
        await member.send("1. Все мы должны исходить из общепринятых правил морали и нравственности, поэтому общение на сервере протекает в свободном русле.
Вы можете выказывать недовольство в сторону администрации безнаказанно, но будьте готовы к тому, что администрация может забанить вас по собственному усмотрению, если посчитает, что вы вредите серверу
2. Запрещается флудить и спамить в каналах командами бота, а так же просто спамить.
3. Реклама соц.сетей,групп и прочего в чатах запрещена без согласования администрации.
4. Реклама других серверов Discord на каналах или в ЛС участникам категорически запрещена.
5. 18+ контент, содержащий особую жестокость и насилие, запрещен (в том числе и завуалированный).
6. Запрещено распространение личных фотографий, информации о пользователях сервера.")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Бета Тест'))
    print('Bot is ready.')


@client.command()
#clear command
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=50):
    await ctx.channel.purge(limit=amount)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Прошу понять и простить 😿")    


@client.command()
#ban command
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
   await ctx.send("Участник успешно забанен")
   await member.ban (reason=reason)
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Прошу понять и простить 😿")  



@client.command()
#mute command
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Отметите участника Сэр!")
        return
    role = discord.utils.get(ctx.guild.roles, name="Chat Muted🤫")
    await ctx.send ("Мут успешно выдОн.")
    await ctx.send ("https://media0.giphy.com/media/HWl1atKEPAWcw/giphy.gif?cid=790b76115d0ba5c44a4e35446b2fe9e4&rid=giphy.gif")
    await member.add_roles(role)

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Прошу понять и простить 😿")

@client.command()
#unmute command
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Отметите участника Сэр!")
        return
    role = discord.utils.get(ctx.guild.roles, name="Chat Muted🤫")
    await ctx.send ("Мут успешно снят.")
    await member.remove_roles(role)       



 

token = os.environ.get('BOT_TOKEN') 
client.run(str(token))
