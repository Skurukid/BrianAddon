import asyncio
async def textcommand(client, channel, message):
    print("Sending shitpost")
    currentChannel = client.get_channel(channel)
    await currentChannel.send(message)
    await client.close()

async def voicecommand(client, textchannel, voicechannel, message):
    print("Playin musac")
    currentText = client.get_channel(textchannel)
    currentVoice = client.get_channel(voicechannel)
    await currentVoice.connect()
    await currentText.send(message)
    await asyncio.sleep(10)
    await client.close()