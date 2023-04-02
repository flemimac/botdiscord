import discord
from discord.ext import commands
import asyncio
import random
from random import randint

client = commands.Bot(command_prefix = ".", intents = discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
	print("s1mba")
	await client.change_presence(status=discord.Status.idle,activity=discord.Game(".help"))

@client.command(pass_context = True)
async def push(ctx, *args):
    role = ctx.guild.get_role(role_id=935513102764625952)
    await ctx.send(f"Ты получил роль: {role.mention}")

#////////////////////////////////////////////

@client.command(pass_context =True)
async def котик (ctx):
	await ctx.channel.purge(limit = 1)
	await ctx.send("https://media.discordapp.net/attachments/906183100520861697/929741668733845554/eat.gif")


@client.command(pass_context=True) #оформление текста
async def help(ctx, *args):
	retStr = ("""```fix\nПриветствие от бота - .hi\nАнекдот про улитку - .улитка\nАнекдот про черепаху - .черепаха\nКинуть монетку - .монета\nКинуть ролл - .roll\nУзнать кто я - .кто_я\n```""")
	embed = discord.Embed(title = "Помощь по боту")
	embed.add_field(name="Снизу представлены команды", value=retStr)
	await ctx.send(embed=embed)

# ////////////АДМИН////////////////

# //////////////////// оформление /////////////////

@client.command(pass_context=True)
async def asd(ctx, *args):
	retStr = ("""```css\n
Группа ВК:
```
> https://vk.com/melonyrust
```
Пермаментная ссылка на Дискорд сервер:
```
> https://discord.gg/KTd3uDkBV5
```
Донат:
```
> в разработке
```
IP сервера:
```
> в разработке
```
Как зайти?
```
> в разработке

**Приятного время провождения на проекте :heart:**
""")
	embed = discord.Embed(title = "Приветствую вас на нашем дискорд сервере Melony Rust. В данном канале находиться основная информация, которая вам пригодиться.", description = retStr, color = 0x71368A)
	#embed.add_field(name="Приветствую вас на нашем дискорд сервере Melony Rust. В данном канале находиться основная информация, которая вам пригодиться.",value=retStr, inline=False)
	embed.set_image(url = 'https://cdn.discordapp.com/attachments/964152024604225566/969559228077465630/melonyrust-1.png')
	await ctx.send(embed=embed)

@client.command(pass_context=True)
async def admin(ctx, *args):
	retStr = ("""```fix\nВыдача кика игроку - .kick ник\nВыдача бана игроку - .ban ник\nВыдача мута игроку - .mute ник время причина\nСнять мут с игрока - .unmute ник\nВыдача страйка игроку - .strike ник причина\nСнять страйк с игрока - .unstrike ник\nЧистка чата - .clear кол-во строк```""")
	retStr2 = ("""```fix\nВыдача кика игроку - .kick ник \nВыдача мута игроку - .mute ник время причина\nСнять мут с игрока - .unmute ник\nВыдача страйка игроку - .strike ник причина\nСнять страйк с игрока - .unstrike ник\nЧистка чата - .clear кол-во строк\n```""")
	embed = discord.Embed(title = "Помощь по боту для администрации")
	embed.add_field(name="Команды для Старшей Модерации",value=retStr, inline=False)
	embed.add_field(name="Команды для Модерации",value=retStr2, inline=False)
	await ctx.send(embed=embed)

#ПРАВИЛА ДИСКОРДА

@client.command(pass_context=True)
async def rulesDS(ctx, *args):
	retStr = ("""```css\n1.1 Запрещено оскорбление кого либо в любом виде, а также оскорблять проект ( искл. высказывание объективной критики с приведением фактов или в шутку). \n[Мут от 1 часа до 7 дней] \n1.2 Запрещена реклама других проектов. \n[Бан навсегда] \n1.3 Запрещено злоупотребление нецензурной лексики. \n[Мут от 1 часа до 7 дней] \n1.4 Запрещен флуд (более 3 однотипных сообщений), флуд гифками, смайлами, пингами, буллингом и т.д. \n[Мут от 1 часа до 7 дней] \n1.5 Запрещены попытки обмана игроков/администрации/модерации. \n[Мут от 1 часа до бана] \n1.6 Запрещен какой-либо обход наказания. \n[От страйка до бана] \n1.7 Запрещен контент 18+. \n[Мут от 1 часа до бана] \n1.8 Запрешенно писать оффтоп в канале или использовать канал не по назначению. \n[Мут от 1 часа до страйка] \n1.9 Запрещено пинговать роли игроков или администрации без причины \n[Мут от 1 часа до кика] \n1.10 Запрещено обсуждать политику и разжигать межрелигиозные и межнациональные розни \n[Мут от 7 дней до пермача]\n```""")
	retStr2 = ("""```css\n2.1 Запрещены чрезмерные крики, включение громких звуков через Soundpad и т.д. \n[Мут от 1 часа до кика] \n2.2 Запрещено прогонять членов администрации из голосовых каналов, если они зашли/пишут по причине. \n[Мут от 1 часа до кика] \n2.3 Запрещено включать музыку в голосовых каналах без согласия всех участников голосового канала. \n[Мут от 1 часа до страйка]```""")
	embed = discord.Embed(title = "Правила Дискорд сервера", color = 0x71368A)
	embed.add_field(name="Общие правила для всех",value=retStr, inline=False)
	embed.add_field(name="Правила для голосовых каналов",value=retStr2, inline=False)
	await ctx.send(embed=embed)

@client.command(pass_context=True)
async def warningDS(ctx, *args):
	retStr = ("""```diff\n- Модерация в праве менять действующие правила без оповещения. \n- Незнание правил не освобождает от ответственности.```""")
	embed = discord.Embed(title = "Помните!", description=retStr, color = 0x71368A)
	await ctx.send(embed=embed)

#ПРАВИЛА СЕРВЕРА

@client.command(pass_context=True)
async def rulesServer(ctx, *args):
	retStr = ("""```css\n1.1 Игрокам запрещено использование и распространение хитростей игры, чит программы/баги/макросы или любые другие средства, что даёт дополнительное преимущество перед другими игроками и не входит в стандартную механику игры. \n[Бан навсегда] \n1.2 Запрещено превышать лимит игроков в команде (лимит 3). \n[Бан от 7 до 30 дней] \n1.3 Запрещено использовать никнеймы администраторов или выдавать себя за администрацию. \n[Бан от 2 до 7 дней] \n1.4 Запрещено застраивать и препятствовать входу РТ, запрещено застраивать дома игроков "усами". \n[От предупреждения до бана 7 дней] \n1.5 Не запрещено обманывать людей при обмене. \n[Бан от 2 до 7 дней] \n```""")
	embed = discord.Embed(title="Правила игрового процесса",description=retStr, color = 0x71368A)
	await ctx.send(embed=embed)

@client.command(pass_context=True) #оформление текста
async def rulesServer2(ctx, *args):
	retStr = ("""```css\n2.1 Запрещен флуд. Флудом считается отправка нескольких одинаковых сообщений в короткий промежуток времени (более 3 в минуту). \n[10 минут/1 час/1 день/7 дней] \n2.2 Запрещено злоупотреблять сообщениями с зажатой кнопкой Caps Lock. \n[10 минут/1 час/1 день/7 дней] \n2.3 Запрещено клеветать на игрока или провоцировать его на агрессию. \n[10 минут/1 час/1 день/7 дней] \n2.4 Запрещено оскорбление администрации, модерации и игроков в любых формах. \n[10 минут/1 час/1 день/7 дней] \n2.5 Запрещены ссылки в чате на сторонние сервисы и сайты. \n[Бан навсегда] \n2.6 Запрещено затрагивать родителей в любых случаях. \n[10 минут/1 час/1 день/7 дней] \n 2.7 Запрещена реклама сторонних проектов и серверов, в любой форме. \n[Бан навсегда] \n 2.8 Запрещено оскорбление проекта \n[Бан навсегда] \n```""")
	embed = discord.Embed(title = "Общение в игровом чате", description=retStr, color = 0x71368A)
	await ctx.send(embed=embed)

@client.command(pass_context=True) #оформление текста
async def rulesServer3(ctx, *args):
	retStr = ("""```css\n3.1 Запрещено использование своего статуса в личных целях (выдача ресурсов себе или игрокам) \n3.2 Запрещена разблокировка игроков без доказательств. \n3.3 Запрещено распространение информации игрокам или любым другим 3м лицам о планах или любых других разговорах касающихся планов проекта или администрации. \n3.4 Запрещено выдавать блокировку или мут любому человеку из состава администрации без обсуждения с главой проекта. \n3.5 Запрещена выдача срока бана выше, чем описано в правилах проекта. \n3.6 Запрещена блокировка если правила нарушены вне проекта. (пример : вы поссорились с игроком в соц. сетях). \n3.7 Запрещено бездействовать когда игрок нарушает правила. \n3.8 Запрещена передача свой аккаунт 3м лицам. \n ```""")
	embed = discord.Embed(title = "Правила для администрации", description=retStr, color = 0x71368A)
	await ctx.send(embed=embed)

@client.command(pass_context=True) #оформление текста
async def rulesServer4(ctx, *args):
	retStr = ("""```css\n4.1 Администрация не возвращает Вам утерянный лут если причина потери не связана с недоработкой проекта. (чтобы произвести возврат Вам нужно предъявить доказательства в виде видео или скриншотов). \n4.2 Вещи которые Вы приобретаете в игровом магазине не подлежат возврату или обмену. \n4.3 Администрация не оказывает помощь в рейдах, строительстве домов и т.д. \n```""")
	embed = discord.Embed(title = "Дополнительно", description=retStr, color = 0x71368A)
	await ctx.send(embed=embed)

@client.command(pass_context=True)
async def warningServer(ctx, *args):
	retStr = ("""```diff\n- Высшая администрация в праве менять действующие правила без оповещения. \n- Незнание правил не освобождает от ответственности.\n- За использование недочетов правил - будете наказаны вдвойне. ```""")
	embed = discord.Embed(title = "Помните!", description=retStr, color = 0x71368A)
	await ctx.send(embed=embed)

#map
@client.command(pass_context=True)
async def map(ctx, *args):
	retStr = ("""```css\n[Начало связи...]\nЗдравия желаю, бойцы!\nМы прислали Вам свежую карту галактики с обозначениями контрлирующих планет. Ознакомиться всем!\nПомните, каждое Ваше действие сопровождается положительным или отрицательным последствием, так что думайте перед тем, что Вы делаете!\nТакже помните, что КНС не будет стоять на месте и будут расширять свои влияния.\nДа прибудет с Вами Сила.\nПоследнее обновние данных 17.02.22.\n[Конец связи...]```""")
	embed = discord.Embed(title = "Карта Галактики", description=retStr)
	embed.set_image(url = 'https://cdn.discordapp.com/attachments/863347474332254208/943926996084338818/a0d56766b171a2ed.png')
	await ctx.send(embed=embed)

# //////////////////// kick /////////////////
@client.command(pass_context=True) # kick
@commands.has_permissions(kick_members=True)
async def kick(ctx,member:discord.Member,*,reason=None):
	await member.kick(reason=reason)

	emb = discord.Embed(title = 'Кик', colour = discord.Color.red() )
	await ctx.channel.purge(limit = 1)

	emb.set_author( name = member.name, icon_url = member.avatar)
	emb.add_field(name = 'Поздравляем', value = 'Игрок {} был кикнут'.format(member.mention))
	emb.set_footer(text = 'Был кикнут администратором {}'.format(ctx.author.name), icon_url = ctx.author.avatar)

	await ctx.send(embed = emb)

# //////////////////// ban /////////////////
@client.command(pass_context=True) # ban
@commands.has_permissions(ban_members=True)

async def ban(ctx,member:discord.Member,*,reason=None):
	emb = discord.Embed(title = 'Бан', colour = discord.Color.red() )
	await ctx.channel.purge(limit = 1)

	await member.ban(reason=reason)

	emb.set_author( name = member.name, icon_url = member.avatar)
	emb.add_field(name = 'Поздравляем', value = 'Игрок {} был забанен'.format(member.mention))
	emb.set_footer(text = 'Был забанен администратором {}'.format(ctx.author.name), icon_url = ctx.author.avatar)

	await ctx.send(embed = emb)

# //////////////////// mute /////////////////

@client.command(pass_context=True) # mute
@commands.has_permissions(manage_roles=True)
async def mute(ctx,member:discord.Member,time:int, reason):
	mute = discord.utils.get(ctx.message.guild.roles, name="Мут")
	await member.add_roles(mute)

	emb = discord.Embed(title = 'Игрок был замучен', colour = discord.Color.red() )
	await ctx.channel.purge(limit = 1)

	emb.set_author(name = member.name, icon_url = member.avatar)
	emb.add_field(name = 'Причина: ', value = reason, inline = False)
	emb.add_field(name = 'Время мута: ', value = f'{time} минут', inline = False)
	emb.set_footer(text = 'Был замучен модератором {}'.format(ctx.author.name), icon_url = ctx.author.avatar)

	await ctx.send(embed = emb)

	await asyncio.sleep(time * 60)
	await member.remove_roles(mute)

# //////////////////// unmute /////////////////
@client.command(pass_context=True) # unmute
@commands.has_permissions(manage_roles=True)
async def unmute(ctx,member:discord.Member):
	mute = discord.utils.get(ctx.message.guild.roles, name="Мут")
	await member.remove_roles(mute)

	emb = discord.Embed(title = 'Игрок размучен', colour = discord.Color.green() )
	await ctx.channel.purge(limit = 1)

	emb.set_author( name = member.name, icon_url = member.avatar)
	emb.set_footer(text = 'Был размучен модератором {}'.format(ctx.author.name), icon_url = ctx.author.avatar)

	await ctx.send(embed = emb)

# //////////////////// clear /////////////////
@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 100):
	await ctx.channel.purge(limit = amount)

# ////////////////// strike /////////////////

@client.command(pass_context=True) # strike
@commands.has_permissions(manage_roles=True)
async def strike(ctx,member:discord.Member, reason):
	strike = discord.utils.get(ctx.message.guild.roles, name="Страйк")
	await member.add_roles(strike)

	emb = discord.Embed(title = 'Игрок получил страйк', colour = discord.Color.red() )
	await ctx.channel.purge(limit = 1)

	emb.set_author(name = member.name, icon_url = member.avatar)
	emb.add_field(name = 'Причина: ', value = reason, inline = False)
	emb.set_footer(text = 'Был выдан модератором {}'.format(ctx.author.name), icon_url = ctx.author.avatar)

	await ctx.send(embed = emb)

	await member.remove_roles(strike)

# //////////////////// unstrike /////////////////
@client.command(pass_context=True) # unstrike
@commands.has_permissions(manage_roles=True)
async def unstrike(ctx,member:discord.Member):
	strike = discord.utils.get(ctx.message.guild.roles, name="Страйк")
	await member.remove_roles(strike)

	emb = discord.Embed(title = 'С игрока снят страйк', colour = discord.Color.green() )
	await ctx.channel.purge(limit = 1)

	emb.set_author( name = member.name, icon_url = member.avatar)
	emb.set_footer(text = 'Был снят модератором {}'.format(ctx.author.name), icon_url = ctx.author.avatar)

	await ctx.send(embed = emb)


#//////////////////// МЕМЫ //////////////////
@client.command(pass_context =True)
async def улитка (ctx):
	await ctx.send('```Улитка заходит в бар, но бармен заявляет: У нас строгая политика в отношении улиток! — и ногой выпихивает ее на улицу.\nЧерез неделю улитка возвращается в бар и говорит бармену: Ну и как я интересно "захожу" в бар, ног то у меня нет.```')
@client.command(pass_context =True)
async def черепаха (ctx):
	await ctx.send('```Заходит черепаха в бар с убитым видом просит стакан воды. Получая, уходит. На следующие сутки снова в бар заходит черепаха и, получив стакан воды, удаляется с всё тем же убитым видом. Такая история повторяется почти неделю и наконец-то бармен не выдерживает испрашивает:\n — Чё такая убитая и зачем тебе, стакан воды?\n На что черепаха рыдая отвечает:\n — Да некогда объяснять, у меня там дом горит…\n```')

#////////////////// TEST ///////////////////

@client.command(pass_context =True)
async def монета (ctx):
	embed = discord.Embed(title= f"Вам выпало - {random.choice(['орёл', 'решка'])}")
	await ctx.send(embed=embed)

@client.command()
async def roll(ctx):
    embed = discord.Embed(title= f"Рандомное число - {randint(0,100)}")
    await ctx.send(embed=embed)

@client.command(pass_context =True)
async def кто_я (ctx):
	embed = discord.Embed(title= f"Вы скорее всего - {random.choice(['вредная картошка', 'спелый огурец', 'вице-адмирал', 'король', 'шевелящийся герой нашего времени', 'дурак', 'соблазнительная марихуана', 'пудж', 'слон', 'кто вы?', 'антилопа', 'продажный федерал', 'какашка!!!'])}")
	await ctx.send(embed=embed)

client.run('Token')