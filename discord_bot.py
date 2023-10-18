import discord
from webscrape import valorant_stats
from discord.ext import commands

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def stats(ctx, username):
    status = valorant_stats(username)
    if status == False:
        await ctx.send("Player not found!")
    else:
        #Read from textfile
        with open ('player_stat.txt', 'r') as file:
            #Read the firstline 
            line = file.readline()
            #create the embed message and fill it with the first line
            embed_message = discord.Embed(title=f"{username}'s stats",description=f"{line}", color=discord.Color.green())
            line=file.readline()
            #Read the second line for the player's profile picture
            
            #Set the embed author to whomever requested it   
            embed_message.set_author(name=f"Request by {ctx.author}", icon_url=ctx.author.avatar)

            #Set the thumbnail to player's profile picture
            embed_message.set_thumbnail(url=f"{line}")

            #Read the last line
            line = file.readline()
            #Split it and store each of it in a array
            line = line.split("#")
            
            #Use a for loop to fill out the rest the embed's fields
            for i in range(0,len(line)-1,2):
                embed_message.add_field(name=line[i], value=line[i+1],inline=True)
        #Send embed
        await ctx.send(embed=embed_message)
            
client.run('discordToken')