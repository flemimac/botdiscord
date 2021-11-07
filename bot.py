import discord
from discord.ext import commands
import asyncio
import datetime

token = "ODc5NDIzMDU0OTE5MzY4NzA0.YSPgiw.blvrUzQ6owDvbv3h2TgENYTuz0Y" # token bot

bot = commands.Bot(command_prefix = ".")
bot.remove_command('help')

@bot.event
async def on_ready():
	print("s1mba")
	await bot.change_presence(status=discord.Status.idle,activity=discord.Game("Garry's mod"))

@bot.command(pass_context =True)
async def hi (ctx):
	await ctx.send("hi {}".format(ctx.message.author.mention))

@bot.command(pass_context=True) #оформление текста
async def help(ctx, *args):
	retStr = ("""```fix\nПриветствие от бота - .hi\nИнформация для КУБ - .information\nАдмин команды - .admin\nАнекдот про улитку - .улитка\nАнекдот про черепаху - .черепаха\n```""")
	embed = discord.Embed(title = "Помощь по боту", colour=discord.Colour.orange())
	embed.add_field(name="Снизу представлены команды", value=retStr)
	await ctx.send(embed=embed)


# ////////////АДМИН////////////////

# //////////////////// оформление /////////////////
@bot.command(pass_context=True)
async def admin(ctx, *args):
	retStr = ("""```fix\nВыдача кика игроку - .kick ник причина\nВыдача бана игроку - .ban ник причина\nВыдача мута игроку - .mute ник (мут на 30 минут)\nСнять мут с игрока - .unmute ник\nЧистка чата - .clear кол-во строк```""")
	embed = discord.Embed(title = "Помощь по боту для администрации", colour=discord.Colour.orange())
	embed.add_field(name="Admin",value=retStr)
	await ctx.send(embed=embed)

@bot.command(pass_context =True)
async def information (ctx):
	embed=discord.Embed(title="Информация бойцам Корпуса Управления Базы", color=0x878787)

	embed.add_field(name="Устав ВАР", value="https://docs.google.com/document/d/1shv7trGNqwmUyZ5pXua_FuggUiQ2rzDWQHI3HahurFM/edit#heading=h.3u6d4hnq9o2g", inline=False)
	embed.add_field(name="Таблица КУБ", value="https://docs.google.com/spreadsheets/d/1G4zSxm2OTDrYtYgKGFGy6XZ7oqW0arOr4QaJpTRLWpU/edit#gid=0", inline=False)
	embed.add_field(name="Справочник по ЗВ", value="https://discord.gg/2bdQJbH", inline=False)
	embed.add_field(name="Документация про ремонт генератора", value="https://docs.google.com/document/d/1S7tWcQwpkB-P3I8yRct2ePlFH6Q1tbAolF4tYRdUT2s/edit?usp=drivesdk", inline=False)
	embed.add_field(name="Документация про взлом консоли", value="https://docs.google.com/document/d/1A7r3CrxAz8Z1zZAqKGLHzECFgKxsTD52oUsWR2R-p1g/edit?usp=drivesdk", inline=False)
	await ctx.send(embed=embed)

# //////////////////// kick /////////////////
@bot.command(pass_context=True) # kick
@commands.has_permissions(kick_members=True)
async def kick(ctx,member:discord.Member,*,reason=None):
	await member.kick(reason=reason)

	emb = discord.Embed(title = 'Кик', colour = discord.Color.red() )
	await ctx.channel.purge(limit = 1)

	emb.set_author( name = member.name, icon_url = member.avatar_url)
	emb.add_field(name = 'Поздравляем', value = 'Игрок {} был кикнут'.format(member.mention))
	emb.set_footer(text = 'Был кикнут администратором {}'.format(ctx.author.name), icon_url = ctx.author.avatar_url)

	await ctx.send(embed = emb)

# //////////////////// ban /////////////////
@bot.command(pass_context=True) # ban
@commands.has_permissions(ban_members=True)

async def ban(ctx,member:discord.Member,*,reason=None):
	emb = discord.Embed(title = 'Бан', colour = discord.Color.red() )
	await ctx.channel.purge(limit = 1)

	await member.ban(reason=reason)

	emb.set_author( name = member.name, icon_url = member.avatar_url)
	emb.add_field(name = 'Поздравляем', value = 'Игрок {} был забанен'.format(member.mention))
	emb.set_footer(text = 'Был забанен администратором {}'.format(ctx.author.name), icon_url = ctx.author.avatar_url)

	await ctx.send(embed = emb)

# //////////////////// mute /////////////////
@bot.command(pass_context=True) # mute
@commands.has_permissions(manage_roles=True)
async def mute(ctx,member:discord.Member):
	mute = discord.utils.get(ctx.message.guild.roles, name="Мут")
	await member.add_roles(mute)

	emb = discord.Embed(title = 'Мут', colour = discord.Color.red() )
	await ctx.channel.purge(limit = 1)

	emb.set_author( name = member.name, icon_url = member.avatar_url)
	emb.add_field(name = 'Поздравляем', value = 'Игрок {} был замучен на пол часа'.format(member.mention))
	emb.set_footer(text = 'Был замучен администратором {}'.format(ctx.author.name), icon_url = ctx.author.avatar_url)

	await ctx.send(embed = emb)

	await asyncio.sleep(1800)
	await member.remove_roles(mute)

# //////////////////// unmute /////////////////
@bot.command(pass_context=True) # unmute
@commands.has_permissions(manage_roles=True)
async def unmute(ctx,member:discord.Member):
	mute = discord.utils.get(ctx.message.guild.roles, name="Мут")
	await member.remove_roles(mute)

	emb = discord.Embed(title = 'Мут снят', colour = discord.Color.green() )
	await ctx.channel.purge(limit = 1)

	emb.set_author( name = member.name, icon_url = member.avatar_url)
	emb.add_field(name = 'Поздравляем', value = 'Игрок {} был размучен'.format(member.mention))
	emb.set_footer(text = 'Был размучен администратором {}'.format(ctx.author.name), icon_url = ctx.author.avatar_url)

	await ctx.send(embed = emb)

# //////////////////// clear /////////////////
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 100):
	await ctx.channel.purge(limit = amount)


#//////////////////// МЕМЫ //////////////////
@bot.command(pass_context =True)
async def улитка (ctx):
	await ctx.send('```Улитка заходит в бар, но бармен заявляет: У нас строгая политика в отношении улиток! — и ногой выпихивает ее на улицу.\nЧерез неделю улитка возвращается в бар и говорит бармену: Ну и как я интересно "захожу" в бар, ног то у меня нет.```')
@bot.command(pass_context =True)
async def черепаха (ctx):
	await ctx.send('```Заходит черепаха в бар с убитым видом просит стакан воды. Получая, уходит. На следующие сутки снова в бар заходит черепаха и, получив стакан воды, удаляется с всё тем же убитым видом. Такая история повторяется почти неделю и наконец-то бармен не выдерживает испрашивает:\n — Чё такая убитая и зачем тебе, стакан воды?\n На что черепаха рыдая отвечает:\n — Да некогда объяснять, у меня там дом горит…\n```')

#////////////////// TEST ///////////////////

bot.run(token)