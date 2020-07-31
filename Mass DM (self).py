import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('(whatever u wanna send the users)')
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('(your token goes here)', bot=False)
