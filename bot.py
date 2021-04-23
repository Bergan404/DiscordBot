import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')

# client = discord.Client()

# @client.event
# async def on_ready():
#   print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     if message.content.startswith('!set'):
#       embedVar = discord.Embed(title='**Game**', description="Desc", color=discord.Colour.random())
#       embedVar.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
#       # embedVar.add_field(name="Field1", value="hi", inline=False)
#       # embedVar.add_field(name="Field2", value="hi2", inline=False)
#       await message.channel.send(embed=embedVar)

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )


# client.run(os.environ['TOKEN'])
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Discord server!'
    )

@bot.command(name='set')
async def set(ctx, game, time):
  embedVar = discord.Embed(title=game, description=time, color=discord.Colour.random())
  embedVar.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
  embedVar.add_field(name="Who's Joining", value="hi", inline=False)
  # embedVar.add_field(name="Field2", value="hi2", inline=False)
  await ctx.send(embed=embedVar)

bot.run(TOKEN)
