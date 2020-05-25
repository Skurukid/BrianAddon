## BrianAddon
Make your discord bot talk shit for you. 
## Why even bother?
You can easily create hotkeys so shitposting is only one click away. You can even create cronjobs, so once Wednesday comes you can bet your ass that all your dudes will know about this.
## Requirements
You'll need Discord and PyNaCl packages, so </br>
```pip install discord pynacl``` </br>
should be enough. </br>
Oh, and don't forget to fill out literally only thing in config file. You know where to get your bot's token, right? Just put it there and you should be fine.
## Voice commands
Yeah, well, that was supposed to run Groovy commands, but according to their support team, there's no way it will take commands from other bots, so it's not working currently. Maybe someday. 
## Help
```Options:
  -h, --help            show this help message and exit
  -l, --list            Print list of channels
  -c PREDEFCHANNEL, --channel=PREDEFCHANNEL
                        Choose index of predefined channel to send message to.
                        For list of channel run thisscript with -l option
  -v VOICECHANNEL       Choose index of predefined voice channel to play
                        groovy to.For list of channels run this script with -l
                        option
  -m PREDEFMESSAGE, --message=PREDEFMESSAGE
                        Write predefined message
  -t COMMANDTYPE, --type=COMMANDTYPE
                        Choose command type, either t (text command) or v
                        (voice command)````
