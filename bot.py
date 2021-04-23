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
async def set(ctx, game, time, message='@everyone'):
  embedVar = discord.Embed(title=game, description=time, color=discord.Colour.random())
  embedVar.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
  embedVar.add_field(name="Who's Joining", value='Message if you are joining!', inline=False)
  await ctx.send(message, embed=embedVar)

@bot.command(name="--help", description="Returns all commands available")
async def help(ctx):
    helptext = "```"
    for command in ctx.bot.commands:
        helptext+="!set '<game_name>' time\n"
    helptext+="```"
    await ctx.send(helptext)

# @bot.command(pass_context = True)
# async def poll(self, question, *options: str):
#   if len(options) <= 1:
#       await self.send("```Error! A poll must have more than one option.```")
#       return
#   if len(options) > 2:
#       await self.send("```Error! Poll can have no more than two options.```")
#       return

#   if len(options) == 2 and options[0] == "yes" and options[1] == "no":
#       reactions = ['0', '1']
#   else:
#       reactions = ['0', '1']

#   description = []
#   for x, option in enumerate(options):
#       description += '\n {0} {1}'.format(reactions[x], option)

#   embed = discord.Embed(title = question, color = 3553599, description = ''.join(description))

#   react = await self.send(embed = embed)

#   for reaction in reactions[:len(options)]:
#       await self.message.add_reaction(react)

#   embed.set_footer(text='Poll ID: {}'.format(react.id))

#   await self.edit_message(react, embed=embed)

bot.run(TOKEN)
