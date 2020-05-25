import asyncio
import discord

async def textcommand(client, channel, message):
    print("Sending shitpost")
    currentChannel = client.get_channel(channel)
    await currentChannel.send(message)
    await client.close()

async def piccommand(client, channel, message, pic):
    print("Sending nudes")
    currentChannel = client.get_channel(channel)
    if message == " ":
        await currentChannel.send(file=discord.File("./pics/" + pic))
    else:
        await currentChannel.send(message, file=discord.File("./pics/" + pic))


async def voicecommand(client, textchannel, voicechannel, message):
    print("Playin musac")
    currentText = client.get_channel(textchannel)
    currentVoice = client.get_channel(voicechannel)
    await currentVoice.connect()
    await currentText.send(message)
    await asyncio.sleep(10)
    await client.close()