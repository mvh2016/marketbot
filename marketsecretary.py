import discord
from discord.ext import commands
from os import environ

client = commands.Bot(command_prefix = '/')
game = discord.Game("in goodstuff!")
lastHost = ''
lastStarting = ''
lastMessageID = ''
lastTitle = ''
discordToken = environ.get('discordToken')

@client.event
async def on_ready():
    print ('Bot is ready.')
    await client.change_presence(activity=game)
    embed = discord.Embed(
       title = '**Bot is Online**',
       colour = discord.Colour.green()
    )
        
    channel = client.get_channel(664965790037966897)
    await channel.send(embed=embed)

@client.command()
async def commands(ctx):
    
    embed = discord.Embed(
        title = '**How to Use the Market Secretary Bot**',
        colour = discord.Colour.blue(),
        description = 'A simple list of commands and their correct usage!'
    )
    
    embed.add_field(name = '/sessionstart <Start Time> "<Any Notes>"' , value = 'Sends a Supermarket Session start notification. \n Remember to use quotations for the Any Notes section. \n e.g. `/sessionstart 00:00 "Fall in near the gate!`"', inline = 'false')    
    embed.add_field(name = '/sessionend "<Any Notes>"', value = 'Sends a Supermarket Session end notification. \n Remember to use quotations for the Any Notes section. \n e.g. `/sessionend "Thank you for attending!"`', inline = 'false')
    embed.add_field(name = '/recruitmentstart <Start Time> "<Any Notes"', value = 'Sends a Recruitment Session start notification. \n Remember to use quotations for the Any Notes section. \n e.g. `/recruitmentstart 00:00 "Fall in near the gate!`"', inline = 'false')
    embed.add_field(name = '/recruitmentend "<Any Notes>"', value = 'Sends a Recruitment Session end notification. \n Remember to use quotations for the Any Notes section. \n e.g. `/recruitmentend "Thank you for attending!"`', inline = 'false')
    
    await ctx.send(embed=embed)

@client.command()
async def sessionstart(ctx, arg1, arg2):

    role = discord.utils.get(ctx.guild.roles, name="Event Host")
    
    if role not in ctx.author.roles:
        await ctx.send(':warning: Insufficient permissions - role required: `Event Host` '+ctx.message.author.mention)
    else:
        messageAuthor = ctx.message.author.mention
        embed = discord.Embed(
            title = '**:calendar: Supermarket Session Scheduled :calendar:**',
            colour = discord.Colour.purple()
        )
        embed.add_field(name = 'Host', value = '{}'.format(messageAuthor), inline = 'false')
        embed.add_field(name = 'Starting At', value = '{}'.format(arg1), inline = 'false')
        embed.add_field(name = 'Host\'s Notes', value = '{}'.format(arg2), inline = 'false')
    
        channel = client.get_channel(665180552005025802)
        await channel.send(embed=embed)
        await channel.send('<@&663183646374494208>')
        await ctx.send(':white_check_mark: Event successfully posted, '+ctx.message.author.mention)

@client.command()
async def sessionend(ctx, arg):

    role = discord.utils.get(ctx.guild.roles, name="Event Host")
    
    if role not in ctx.author.roles:
        await ctx.send(':warning: Insufficient permissions - role required: `Event Host` '+ctx.message.author.mention)
    else:
        messageAuthor = ctx.message.author.mention
        embed = discord.Embed(
            title = '**:alarm_clock: Supermarket Session Ended :alarm_clock:**',
            colour = discord.Colour.purple()
        )
        embed.add_field(name = 'Hosted By', value = '{}'.format(messageAuthor), inline = 'false')
        embed.add_field(name = 'Host\'s Notes', value = '{}'.format(arg), inline = 'false')
    
        channel = client.get_channel(665180552005025802)
        await channel.send(embed=embed)
        await ctx.send(':white_check_mark: Event successfully posted, '+ctx.message.author.mention)

@client.command()
async def recruitmentstart(ctx, arg1, arg2):

    role = discord.utils.get(ctx.guild.roles, name="Event Host")
    
    if role not in ctx.author.roles:
        await ctx.send(':warning: Insufficient permissions - role required: `Event Host` '+ctx.message.author.mention)
    else:
        messageAuthor = ctx.message.author.mention
        embed = discord.Embed(
            title = '**:calendar: Recruitment Session Scheduled :calendar:**',
            colour = discord.Colour.purple()
        )
        embed.add_field(name = 'Host', value = '{}'.format(messageAuthor), inline = 'false')
        embed.add_field(name = 'Starting At', value = '{}'.format(arg1), inline = 'false')
        embed.add_field(name = 'Host\'s Notes', value = '{}'.format(arg2), inline = 'false')
    
        channel = client.get_channel(665180552005025802)
        await channel.send(embed=embed)
        await channel.send('<@&663183646374494208>')
        await ctx.send(':white_check_mark: Event successfully posted, '+ctx.message.author.mention)

@client.command()
async def recruitmentend(ctx, arg):

    role = discord.utils.get(ctx.guild.roles, name="Event Host")
    
    if role not in ctx.author.roles:
        await ctx.send(':warning: Insufficient permissions - role required: `Event Host` '+ctx.message.author.mention)
    else:
        messageAuthor = ctx.message.author.mention
        embed = discord.Embed(
            title = '**:alarm_clock: Recruitment Session Ended :alarm_clock:**',
            colour = discord.Colour.purple()
        )
        embed.add_field(name = 'Hosted By', value = '{}'.format(messageAuthor), inline = 'false')
        embed.add_field(name = 'Host\'s Notes', value = '{}'.format(arg), inline = 'false')
    
        channel = client.get_channel(665180552005025802)
        await channel.send(embed=embed)
        await ctx.send(':white_check_mark: Event successfully posted, '+ctx.message.author.mention)
        
    
client.run(discordToken)
