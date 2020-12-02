import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('MESSAGE HERE')
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('Nzc4NTkzODIxNDU2OTkwMjE4.X7UQAA.CyNvRLfsQ-ctN0fmbarCu9sM_3k', bot=False)
