import keep_alive
import discord
import platform
import time
import configparser
import asyncio
import random
import json
import os
import re
from discord import Member
from discord.ext import commands
from datetime import datetime
from discord.ext.commands import has_permissions, MissingPermissions

#whats the time bitch
def current_time():
	ctime = datetime.now().strftime('[%H:%M:%S] ')
	return ctime

#sets prefix
client = commands.Bot(command_prefix = "m!") #Prefix is "m!", set here.

client.owner_id = 420879711779028993

client.remove_command('help')

#reads lists from files
f = open("SMF Data/bully.txt", "r")
bully = f.read().splitlines()
f = open("SMF Data/stupidface.txt", "r")
stupidface = f.read().splitlines()
f = open("SMF Data/stupidface_response.txt", "r")
stupidface_response = f.read().splitlines()
f = open("SMF Data/csgo.txt", "r")
csgo = f.read().splitlines()
f = open("SMF Data/badbot.txt", "r")
badbot = f.read().splitlines()
f = open("SMF Data/dyno.txt", "r")
dyno = f.read().splitlines()
f = open("SMF Data/8ball.txt", "r")
_8ball = f.read().splitlines()
f.close
for x in _8ball:
  x = x.replace("(n)","\n")

#helpful functions
#nothing here right now

#actual events
@client.event
async def on_ready():
    print(str(client.user.name) + " is ready.")
    user = await client.fetch_user(client.owner_id)
    print("This bot is owned by: " + str(user.name))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(f"League of Losers on {len(client.guilds)} servers."))

@client.event
async def on_member_join(user):
    print(str(user.name) + " joined guild " + str(user.guild))

@client.event
async def on_member_update(before, after):
    if after.id == client.user.id and before.nick != after.nick:
        await after.guild.me.edit(nick = "Spore 2")

@client.event
async def on_message(message):
    await client.process_commands(message)#DONT DELETE THIS LINE MOTHERFUCKER
    custom_emojis = re.findall(r'<:\w*:\d*>', message.content)#puts all the custom emojis in a list

    if message.author == client.user:#doesnt respond to itself
        return
    
    if message.guild.id == 768728434972557342:#doesnt talk in jrahs2024 for censourship reasons
        return

    if message.author.id == 155149108183695360:#when dyno talks tell it that its gay
        dynouser = await client.fetch_user(155149108183695360)
        response = random.choice(dyno)
        await message.channel.send(response.format(x=dynouser.mention))
        return

    if message.author.id == 616030035123634186:
        if random.randrange(1,20) == 1:
            await message.channel.send("dylan ur fat")
    
    if message.author.id == 415763406310866953:
        if random.randrange(1,20) == 1:
            await message.channel.send("i agree with pat")#"pretty interesting man but im using a telescope right now and i cant find anyone who fucking asked"
    
    if message.author.id == 720546849953546271:
        if random.randrange(1,5) == 1:
            await message.channel.send("fuck you ethan")

    if message.content.lower().startswith("ok but when"):#ok but when
        if message.author.id == 420879711779028993:#kevin du
            await message.channel.send("nobody asked dipshit")
        elif message.author.id == 415763406310866953:#patrick kyaw
            await message.channel.send("ok pat u literally look like a pancake")
        elif message.author.id == 616030035123634186:#dylan
            await message.channel.send("stfu yik u dont have a hairline")
        elif message.author.id == 450971118317076491:#elgay
            await message.channel.send("ok elwin this is you right\nhttps://cdn.discordapp.com/attachments/904158261291397162/904629881785184297/20211101_181604.jpg")
        else:
            await message.channel.send("u suck")

    for word in message.content.lower().split():#rush b meme haha funny
        if word in csgo:
            await message.channel.send(":green_square::green_square::green_square::black_large_square::black_large_square::green_square::black_large_square::green_square::black_large_square::black_large_square::green_square::green_square::green_square::black_large_square::black_large_square::green_square::black_large_square::green_square::black_large_square::black_large_square::b::b::black_large_square:\n:green_square::black_large_square::green_square::black_large_square::black_large_square::green_square::black_large_square::green_square::black_large_square::black_large_square::green_square::black_large_square::black_large_square::black_large_square::black_large_square::green_square::black_large_square::green_square::black_large_square::black_large_square::b::black_large_square::b:\n:green_square::green_square::green_square::black_large_square::black_large_square::green_square::black_large_square::green_square::black_large_square::black_large_square::green_square::green_square::green_square::black_large_square::black_large_square::green_square::green_square::green_square::black_large_square::black_large_square::b::b::b:\n:green_square::green_square::black_large_square::black_large_square::black_large_square::green_square::black_large_square::green_square::black_large_square::black_large_square::black_large_square::black_large_square::green_square::black_large_square::black_large_square::green_square::black_large_square::green_square::black_large_square::black_large_square::b::black_large_square::b:\n:green_square::black_large_square::green_square::black_large_square::black_large_square::black_large_square::green_square::black_large_square::black_large_square::black_large_square::green_square::green_square::green_square::black_large_square::black_large_square::green_square::black_large_square::green_square::black_large_square::black_large_square::b::b::black_large_square:")
            return
        elif word == "communism":
            print('COMMUNISM DECTECTED')
            await message.channel.send("https://www.youtube.com/watch?v=U06jlgpMtQs")
            return
        elif word == "epilepsy":
            await message.channel.send("shhhh there's supposed to be a gif here")
            return
        elif word == "69":
            await message.add_reaction(u"\u264B")
            return
        elif word in ["seggs", "seg", "sex", "sexxs"]:
            await message.channel.send("I LOVE SEX SEX SEGGS WHERE U DO THE SEGGS SEGGS")
            #await message.author.edit(nick = "seggs")

    for x in bully:#i do not support bullying in any way
        if str(x) in message.content.lower():
            await message.channel.send("i love bullying")
            return

    for x in stupidface:#krapsje
        for x in custom_emojis:
            message.content = message.content.replace(x,"")
        if str(x) in message.content.lower():
            response = random.choice(stupidface_response)
            await message.channel.send(response.format(x=x))
            return

    for x in badbot:#what u say about my bot
        if str(x) in message.content.lower() and message.author.id != 420879711779028993:
            await message.channel.send("⠄⢸⣿⡟⠛⠛⠃⢸⣿⡇⠄⠄⣿⡇⠄⣼⣿⠟⠻⣿⣆⠄⣿⣿⢠⣾⣿⠋⠄⠄\n⠄⢸⣿⣷⣶⣶⠄⢸⣿⡇⠄⠄⣿⡇⠄⣿⡏⠄⠄⠄⠄⠄⣿⣿⣿⣿⣇⠄⠄⠄\n⠄⢸⣿⡇⠄⠄⠄⠘⣿⣧⣀⣰⣿⡇⠄⢿⣿⣀⣠⣿⡶⠄⣿⣿⠃⢹⣿⣆⠄⠄ \n⠄⠘⠛⠃⠄⠄⠄⠄⠘⠛⠛⠛⠋⠄⠄⠈⠛⠛⠛⠛⠁⠄⠛⠛⠄⠄⠛⠛⠃⠄ \n⠄⠄⠄⠄⢠⣤⡄⠄⠄⣤⣤⠄⢀⣠⣤⣄⡀⠄⢠⣤⡄⠄⠄⣤⣤⠄⠄⠄⠄⠄ \n⠄⠄⠄⠄⠄⢻⣿⣄⣼⣿⠃⣰⣿⠟⠛⢿⣿⡄⢸⣿⡇⠄⠄⣿⣿⠄⠄⠄⠄⠄ \n⠄⠄⠄⠄⠄⠄⠻⣿⡿⠁⠄⣿⣿⠄⠄⢸⣿⡇⢸⣿⡇⠄⠄⣿⣿⠄⠄⠄⠄⠄ \n⠄⠄⠄⠄⠄⠄⠄⣿⡇⠄⠄⠹⣿⣦⣤⣼⣿⠃⠄⣿⣷⣤⣴⣿⡏⠄⠄⠄⠄⠄ \n⠄⠄⠄⠄⠄⠄⠄⠛⠃⠄⠄⠄⠈⠛⠛⠋⠁⠄⠄⠈⠙⠛⠛⠉⠄⠄⠄⠄⠄⠄")
            return

    if "good bot" in message.content.lower():#<3
        await message.channel.send("<3")

#help command
@client.command(aliases=["help"],pass_context=True)
async def hell(ctx):
    helpnumber = str(ctx.message.content)
    if helpnumber == "m!help":
        embed = discord.Embed(
            title="SporeBot help table",
            description="The table for SporeBot help. Duh.",
            color=discord.Color.purple()
        )

        embed.add_field(name="General commands",value="Do m!help 1",inline=False)
        embed.add_field(name="Games",value="Do m!help 2",inline=False)
        embed.add_field(name="Administrator",value="Do m!help admin",inline=False)

        await ctx.send(embed=embed)
    
    elif helpnumber == "m!help 1":
        embed = discord.Embed(
            title="General help table",
            description="General commands include:",
            color=discord.Color.green()
        )

        embed.add_field(name="m!help (number)",value="I mean, you already know what this is.",inline=False)
        embed.add_field(name="m!ping",value="Returns your ping.",inline=False)
        embed.add_field(name="m!8ball (string)",value="Play 8ball!",inline=False)
        embed.add_field(name="m!16ball (string)",value="8ball but he develouped cancer.",inline=False)
        embed.add_field(name="m!kill (@user)",value="Kill someone!",inline=False)

        await ctx.send(embed=embed)
    
    elif helpnumber == "m!help 2":
        await ctx.send("under construction....brrrrrrrrr")
    
    elif helpnumber == "m!help admin":
        embed = discord.Embed(
            title="Administrator help table",
            description="Admin commands include:",
            color=discord.Color.red()
            )

        embed.add_field(name="m!purge (number up to 10 and definitly not including 69)",value="Deletes the last (number) messages",inline=False)

        await ctx.send(embed=embed)

#kill command
@client.command(aliases=["kill"])
async def execute(ctx, member : discord.Member):
    await ctx.send(str(member.mention) + " has died due to being sat on by Dylan.")

#purge command
@client.command(name="purge")
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount):
    if int(amount) <= 10:
        await ctx.channel.purge(limit=int(amount))
    asyncio.sleep(1)
    if int(amount) == 1:
        await ctx.send("Purged " + str(amount) + " message.")
    if int(amount) <= 10 and int(amount) > 1:
        await ctx.send("Purged " + str(amount) + " messages.")
    if int(amount) > 10:
        if int(amount) == 69:
            await ctx.send("Nice. You can't do that though. The limit is 10.")
        else:
            await ctx.send("You can't purge " + str(amount) + " messages! The limit is 10!")

#ping command
@client.command()
async def ping(ctx):
    start_time = time.time()
    message = await ctx.send("Testing Ping...")
    end_time = time.time()
    await message.edit(content="Your ping is: " + str(round(client.latency * 1000)) + "ms.\nAPI: " + str(round((end_time - start_time) * 1000)) + "ms.")

#8ball
@client.command(aliases=['8ball'])
async def eightball(ctx, *, question):
    if random.randrange(1,10) == 1 and not "please" in question.lower().split():
        await ctx.send("ask more politely and maybe i'll answer, fucker")
        return
    await ctx.send(f"{question}\n{random.choice(_8ball)}")

#16ball
@client.command(aliases=['16ball'])
async def sixteenball(ctx, *, question):
    await ctx.send(f"{question}\n{random.choice(_8ball)} {random.choice(_8ball)}")

keep_alive.keep_alive()

#omg its token boy
client.run(os.environ['tokenboy'])