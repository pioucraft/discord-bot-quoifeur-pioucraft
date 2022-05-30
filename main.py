import discord

client = discord.Client()


@client.event
async def on_ready():
    print("le bot est pret")

@client.event
async def on_message(message):
    if message.content.endswith('quoi') or message.content.endswith('quoi?') or message.content.endswith('quoi ?') or message.content.endswith('Quoi?') or message.content.endswith('Quoi') or message.content.endswith('Quoi ?'):
        await message.channel.send("feur")
        print("feur")



client.run(TOKEN)
