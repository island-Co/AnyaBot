import os
import event
import discord
client = discord.Client()
TOKEN = os.environ['TOKEN']
@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)
@client.event
async def on_message(message):
  msg_txt = message.content
  msg_author = message.author
  
  if msg_author.bot:
    return
  if msg_txt in event.hello:
    await message.channel.send(f'{msg_author.mention}さん、おはやいます')

client.run(TOKEN)