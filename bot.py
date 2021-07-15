import discord
from discord.ext import commands
import random, string
from asyncio import sleep
from discord_components import DiscordComponents, Button, ButtonStyle
import os

client = commands.Bot(command_prefix='#')

@client.event
async def on_ready():
    print('gg gen bot activated')
    DiscordComponents(client)
    



     
    while True:
          await client.change_presence(status = discord.Status.online, activity= discord.Activity(name=f'хентай 2021 без смс и регестрации', type= discord.ActivityType.watching))
          await sleep(5)
          guilds = await client.fetch_guilds(limit = None).flatten()
          await client.change_presence(status = discord.Status.online, activity= discord.Activity(name=f'за {len(guilds)} серверами.', type= discord.ActivityType.watching))
          await sleep(5)


@client.command()
async def PHPGen(ctx,member:discord.Member = None):

    if member == None:
        member = ctx.author
    emb = discord.Embed(title='**SosiskaG3N#1311** подарил вам PornHub Premium на **1 месяц**',color=0xff0000)
    emb.set_author(name="Вам подарили подписку", icon_url="https://cdn.discordapp.com/attachments/864113956179804170/865242164559872060/c8b1cb116bee0c99.jpg")
    emb.add_field(name="Закончиться через", value="48 часов", inline=False)
    await ctx.message.delete()
    
    await member.send(embed=emb,components = [
     Button(style=ButtonStyle.green,label='Принять',emoji='✔')
    ]
    )

    response = await client.wait_for('button_click')
    if response.component.label == 'Принять':

        await response.respond(content='https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')

@client.command()
async def PHPGen1(ctx,member:discord.Member = None):

    if member == None:
        member = ctx.author
    emb = discord.Embed(title='**SosiskaG3N#1311** подарил вам PornHub Premium на **1 год**',color=0xff0000)
    emb.set_author(name="Вам подарили подписку", icon_url="https://cdn.discordapp.com/attachments/864113956179804170/865242164559872060/c8b1cb116bee0c99.jpg")
    emb.add_field(name="Закончиться через", value="48 часов", inline=False)
    await ctx.message.delete()
    
    await member.send(embed=emb,components = [
     Button(style=ButtonStyle.green,label='Принять',emoji='✔')
    ]
    )

    response = await client.wait_for('button_click')
    if response.component.label == 'Принять':

        await response.respond(content='https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')

@client.command()
async def NCGen(ctx,member:discord.Member = None):

    if member == None:
        member = ctx.author
    emb = discord.Embed(title='**SosiskaG3N#1311** подарил вам Nitro Classic на **1 месяц**',color=0xff0000)
    emb.set_author(name="Вам подарили подписку", icon_url="https://d33wubrfki0l68.cloudfront.net/af917b75e7f1f34ad53088863e88d46cdd821d04/eaa84/assets/nitro.png")
    emb.add_field(name="Закончиться через", value="48 часов", inline=False)
    await ctx.message.delete()
    
    await member.send(embed=emb,components = [
     Button(style=ButtonStyle.green,label='Принять',emoji='✔')
    ]
    )

    response = await client.wait_for('button_click')
    if response.component.label == 'Принять':

        await response.respond(content='https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')


@client.command()
async def NCGen1(ctx,member:discord.Member = None):

    if member == None:
        member = ctx.author
    emb = discord.Embed(title='**SosiskaG3N#1311** подарил вам Nitro Classic на **1 год**',color=0xff0000)
    emb.set_author(name="Вам подарили подписку", icon_url="https://d33wubrfki0l68.cloudfront.net/af917b75e7f1f34ad53088863e88d46cdd821d04/eaa84/assets/nitro.png")
    emb.add_field(name="Закончиться через", value="48 часов", inline=False)
    await ctx.message.delete()
    
    await member.send(embed=emb,components = [
     Button(style=ButtonStyle.green,label='Принять',emoji='✔')
    ]
    )

    response = await client.wait_for('button_click')
    if response.component.label == 'Принять':

        await response.respond(content='https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')

@client.command()
async def NBGen(ctx,member:discord.Member = None):

    if member == None:
        member = ctx.author
    emb = discord.Embed(title='**SosiskaG3N#1311** подарил вам Nitro Boost на **1 месяц**',color=0xff0000)
    emb.set_author(name="Вам подарили подписку", icon_url="https://d33wubrfki0l68.cloudfront.net/af917b75e7f1f34ad53088863e88d46cdd821d04/eaa84/assets/nitro.png")
    emb.add_field(name="Закончиться через", value="48 часов", inline=False)
    await ctx.message.delete()
    
    await member.send(embed=emb,components = [
     Button(style=ButtonStyle.green,label='Принять',emoji='✔')
    ]
    )

    response = await client.wait_for('button_click')
    if response.component.label == 'Принять':

        await response.respond(content='https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')

@client.command()
async def NBGen1(ctx,member:discord.Member = None):

    if member == None:
        member = ctx.author
    emb = discord.Embed(title='**SosiskaG3N#1311** подарил вам Nitro Boost на **1 год**',color=0xff0000)
    emb.set_author(name="Вам подарили подписку", icon_url="https://d33wubrfki0l68.cloudfront.net/af917b75e7f1f34ad53088863e88d46cdd821d04/eaa84/assets/nitro.png")
    emb.add_field(name="Закончиться через", value="48 часов", inline=False)
    await ctx.message.delete()
    
    await member.send(embed=emb,components = [
     Button(style=ButtonStyle.green,label='Принять',emoji='✔')
    ]
    )

    response = await client.wait_for('button_click')
    if response.component.label == 'Принять':

        await response.respond(content='https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')

@client.command()
async def Sp0tGen(ctx,member:discord.Member = None):

    if member == None:
        member = ctx.author
    emb = discord.Embed(title='**SosiskaG3N#1311** подарил вам Spotify Premium на **1 месяц**',color=0xff0000)
    emb.set_author(name="Вам подарили подписку", icon_url="https://cdn.discordapp.com/attachments/864113956179804170/865254335792021544/rNbw3kG8Pk6NESusnKqZRHGA3lxpZTuwBpCB4nV0eURxtodfVQ1rZS2rpTahEEqYazh7IRBicRg5V5u9ybaSbZQsgmpxmvhJk40w.png")
    emb.add_field(name="Закончиться через", value="48 часов", inline=False)
    await ctx.message.delete()
    
    await member.send(embed=emb,components = [
     Button(style=ButtonStyle.green,label='Принять',emoji='✔')
    ]
    )

    response = await client.wait_for('button_click')
    if response.component.label == 'Принять':

        await response.respond(content='https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')

@client.command()
async def N0rdGen(ctx,member:discord.Member = None):

    if member == None:
        member = ctx.author
    emb = discord.Embed(title='**SosiskaG3N#1311** подарил вам NordVPN на **1 месяц**',color=0xff0000)
    emb.set_author(name="Вам подарили подписку", icon_url="https://s1.nordcdn.com/nordvpn/media/1.88.0/images/meta/nordvpn-default.png")
    emb.add_field(name="Закончиться через", value="48 часов", inline=False)
    await ctx.message.delete()
    
    await member.send(embed=emb,components = [
     Button(style=ButtonStyle.green,label='Принять',emoji='✔')
    ]
    )

    response = await client.wait_for('button_click')
    if response.component.label == 'Принять':

        await response.respond(content='https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')

@client.command()
async def M1neGen(ctx,member:discord.Member = None):

    if member == None:
        member = ctx.author
    emb = discord.Embed(title='**SosiskaG3N#1311** подарил вам Minecraft',color=0xff0000)
    emb.set_author(name="Вам подарили подписку", icon_url="https://image.api.playstation.com/vulcan/img/cfn/11307x4B5WLoVoIUtdewG4uJ_YuDRTwBxQy0qP8ylgazLLc01PBxbsFG1pGOWmqhZsxnNkrU3GXbdXIowBAstzlrhtQ4LCI4.png")
    emb.add_field(name="Закончиться через", value="48 часов", inline=False)
    await ctx.message.delete()
    
    await member.send(embed=emb,components = [
     Button(style=ButtonStyle.green,label='Принять',emoji='✔')
    ]
    )

    response = await client.wait_for('button_click')
    if response.component.label == 'Принять':

        await response.respond(content='https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')

@client.command()
async def nitroGEN(ctx,nitroint:int = None):
    if nitroint == None:
        nitroint = 1
    amount = nitroint
    value = 1
    while value <= amount:
          code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
          await ctx.send(f'{code}\n')      
          value += 1

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)




@client.command()
async def помощь(ctx):
       embed=discord.Embed(title="Команды!", color=0xfbff00)
       embed.add_field(name="#PHPGen", value="Генерирует Подписку PH на 1 месяц", inline=False)
       embed.add_field(name="#PHPGen1", value="Генерирует Подписку PH на 1 год ", inline=False)
       embed.add_field(name="#NCGen", value="Генерирует Подписку Nitro Classic на 1 месяц", inline=False)
       embed.add_field(name="#NCGen1", value="Генерирует Подписку Nitro Classic на 1 год", inline=False)
       embed.add_field(name="#NBGen", value="Генерирует Подписку Nitro Boost на 1 месяц", inline=False)
       embed.add_field(name="#NBGen1", value="Генерирует Подписку Nitro Boost на 1 год", inline=False)
       embed.add_field(name="#Sp0tGen", value="Генерирует Аккаунт Spotify Premium на 1 месяц", inline=False)
       embed.add_field(name="#N0rdGen", value="Генерирует Аккаунт NordVPN на 1 месяц", inline=False)
       embed.add_field(name="#M1neGen", value="Генерирует Аккаунт Minecraft", inline=False)
       embed.add_field(name="#nitroGEN", value="Генерирует Нитро Ссылки", inline=False)

       await ctx.send(embed=embed)

token = os.environ.get('BOT_TOKEN')

client.run(str(token))
