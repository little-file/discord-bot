#pover by little-file
#github: https://github.com/little-file/
import discord,random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("hi"):
        await message.channel.send('Hello')

    if message.content.startswith(">>passworld-ganerade"):
        u = "QWERTYUIOPASDFGHJKLZXCVBNM"

        d = "qazwsxedcrfvtgbyhnujmikol"

        s = "!@#$%^&*()_+-=`~[{]}\|;:/?.>,<"

        n = "0123456789"

        all=u+d+s+n

        l = 16

        p = "".join(random.sample(all,l))

        await message.channel.send("passworld: "+ p)

client.run("your token")