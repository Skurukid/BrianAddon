import discord
from optparse import OptionParser
import configparser
import bullshit
from os import listdir
from os.path import isfile, join

client = discord.Client()

knownTypes = ['t','v','p']
chosenMessage = ''
chosenChannel = int
chosenChannelVoice = int
chosenPic = ''
chosenType = ''

##################################
##########Config Parser###########

cfg = configparser.ConfigParser()
cfg.read('config.conf')

token = cfg["Literally Everything"]["Token"]

##################################
##################################

##################################
##########Option Parser###########

parser = OptionParser()
parser.add_option("-l", "--list", action="store_true", dest="list", default=False,
                  help="Print list of channels")
parser.add_option("-c", "--channel", type="int", dest="preDefChannel", default=-1,
                  help="Choose index of predefined channel to send message to. For list of channel run this"
                       "script with -l option")
parser.add_option("-v", type="int", dest="voiceChannel", default=-1,
                  help="Choose index of predefined voice channel to play groovy to."
                       "For list of channels run this script with -l option")
parser.add_option("-m", "--message", type="string", dest="preDefMessage", default="",
                  help="Write predefined message")
parser.add_option("-t", "--type", type="string", dest="commandType", default="",
                  help="Choose command type, either t (text command), v (voice command) or p (pic command)")
parser.add_option("-p", "--picture", type="string", dest="picPath", default="",
                  help="Choose picture from pics folder to send")
(options, args) = parser.parse_args()

##################################
##################################

def getmessage():
    print("Write message you want to send:")
    chosenmessage = input()
    return chosenmessage

def gettype():
    print("Provide command type:")
    providedtype = input()
    while providedtype not in knownTypes:
        print("Unkown type, please provide either t for textCommand or v for voiceCommand")
        providedtype = input()
    return providedtype

def getchannel(channellist, type):
    print("Provide",type,"channel index:")
    channelindex = input()
    chosenchannel = ''
    while isinstance(chosenchannel, str):
        try:
            chosenchannel = channellist[int(channelindex)]
        except IndexError:
            chosenchannel = 'Wrong index'
            print(chosenchannel)
            channelindex = input()
        except ValueError:
            chosenchannel = 'Not an int'
            print(chosenchannel)
            channelindex = input()
    return chosenchannel

def listchannels(discordclient):
    voicechannels = []
    textchannels = []
    allchannels = [textchannels, voicechannels]
    for guild in client.guilds:
        print("Channels for ",guild.name)
        print("Text:")
        for channel in guild.text_channels:
            allchannels[0].append(channel)
        for index, room in enumerate(allchannels[0]):
            print(index, room.name)

        print("Voice:")
        for channel in guild.voice_channels:
            allchannels[1].append(channel)
        for index, room in enumerate(allchannels[1]):
            print(index, room.name)

    print("")

    return allchannels

def listpics():
    onlyfiles = [f for f in listdir("./pics") if isfile(join("./pics", f))]
    return onlyfiles

@client.event
async def on_ready():

    if not options.list:
        allchannels = listchannels(client)
        allpics = listpics()
        #Define type
        if options.commandType == '':
            chosenType = gettype()
        else:
            chosenType = options.commandType

        #Define text channel
        if options.preDefChannel == -1:
            chosenChannel = getchannel(allchannels[0], "text")
        else:
            chosenChannel = allchannels[0][options.preDefChannel]

        #Define voice channel
        if chosenType == 'v':
            if options.voiceChannel == -1:
                chosenChannelVoice = getchannel(allchannels[1],"voice")
            else:
                chosenChannelVoice = allchannels[1][options.voiceChannel]

        #Define pic file
        if chosenType == 'p':
            if options.picPath == "":
                print("Pics to choose from:")
                print(allpics)
                chosenPic = input()
                while not isfile("./pics/"+chosenPic):
                    print("No such file, try again")
                    chosenPic = input()
            else:
                chosenPic = options.picPath
                while not isfile("./pics/"+chosenPic):
                    print("No such file, try again")
                    chosenPic = input()

        #Define message
        if options.preDefMessage == '' and not chosenType == 'p':
            chosenMessage = getmessage()
        else:
            chosenMessage = options.preDefMessage

        if chosenType == 't':
            print(chosenChannel)
            print(chosenMessage)
            await bullshit.textcommand(client,chosenChannel.id,chosenMessage)
            await client.close()

        elif chosenType == 'v':
            await bullshit.voicecommand(client,chosenChannel.id,chosenChannelVoice.id,chosenMessage)
            await client.close()

        elif chosenType == 'p':
            print(chosenPic)
            await bullshit.piccommand(client,chosenChannel.id,chosenMessage,chosenPic)
            await client.close()


    else:
        listchannels(client)
        await client.close()


if options.list and options.preDefChannel != -1:
    print("Please don't use -l in conjunction with -c")
    exit()
client.run(token)