import RobotSlave
import datetime
import SYNFlooder
from PIL import Image
from pytesseract import image_to_string
from urllib.request import urlopen
import sys
import io
import requests
import json

#needed for script to be run in any file location, will migrate to database at some point
sys.path.insert(0, '/home/kwazinator/Desktop/GITHUB/DiscordBot/Mainfiles/')

######################################START DEF METHODS##############################################
# for transparency, variables saved to files since program might restart often
def igiveup(channel, message, sender):
    with open('dayandhasconfig.txt', 'r') as file:
        data = file.read()
    if data < str(datetime.datetime.now().day) and datetime.datetime.now().hour >= 15:
        answer = RobotSlave.solve()
        with open('robitsanswers.txt', 'w') as file:
            file.write(answer)
        with open('dayandhasconfig.txt', 'w') as file:
            file.write(str(datetime.datetime.now().day))
    else:
        with open('robitsanswers.txt', 'r') as myfile:
            answer = myfile.read()
    return answer

def whoami(channel, message, sender):
    return "You are you."

def whoamireally(channel, message, sender):
    return "I am he, as you are he, as you are me and we are all together."

def shellcommands(channel, message, sender):
    # try catch block with subprocess in it. XD
    return "comming soon"

def test(channel, message, sender):
    return channel + ' ' + message + ' ' + sender

def google(channel, message, sender):
    return ''


def help(channel, message, sender):
    return "!igiveup: provides a solution to the daily Robot Reboot Challenge\n!apex: provides detailed information about said player in Apex doing an API-Lookup --Usage !apex {player-name}\n!google: google-image-searches 3 images and combines and links --Usage !google {term}\n!ddos sends a TCP SYNFlood attach to destination IP, B/W ~500mbps --Usage !ddos {ipaddress x.x.x.x} {PortNum} {NumPackets}\n!OCR Optical Character Recognition, puts specified JPEG image into text so you can Cntrl-C it, --USAGE !OCR {complete path to .jpg MUST end with direct filename use 'copy link address' when rightclicking}"

def ddos(channel, message, sender):
    if sender == 'chan2#2445' and '!ddos' in message[0:6]:
        message = message[6:]
        try:
            if message == '--help':
                return 'format: !ddos x.x.x.x PortNum NumPackets'
            else:
                message = message.split(' ')
                ip = message[0]
                port = message[1]
                numpack = message[2]
                result = SYNFlooder.main(ip, int(port), int(numpack))
                return result
        except:
            return 'Error occured: please use format !ddos x.x.x.x PortNum NumPackets'
        finally:
            pass
    else:
        return 'You do not have permission to run this command'
         

def OCR(channel, message, sender):
    if '!OCR' in message[0:6]:
        try:
            message = message[5:]
            fd = urlopen(message)
            image_file = io.BytesIO(fd.read())
            return image_to_string(Image.open(image_file))
        except Exception as e:
            print(e)
            return "error occured durring process"
        finally:
            pass
    else:
        return ''

def apex(channel, message, sender):
    if '!apex' in message[0:7]:
        req = requests.Session()
        req.headers.update({'TRN-Api-Key': 'ddf05c3b-818b-470a-91fc-b7d1f4704883',
                                     'Accept': 'application/vnd.api+json'})
        url = 'https://public-api.tracker.gg/apex/v1/standard/profile/5/' + message[6:]
        r = req.get(url)
        data = json.loads(r.text)
        legend_name = str(data['data']['children'][0]['metadata']['legend_name'])
        icon = str(data['data']['children'][0]['metadata']['icon'])
        namer, percentiler, ranker, valuer = ['' for x in range(3)], ['' for x in range(3)], ['' for x in range(3)], ['' for x in range(3)]
        for index, dater in enumerate(data['data']['children'][0]['stats']):
            namer[index] += dater['metadata']['name'] + ' '
            percentiler[index] += str(dater['percentile']) + ' '
            ranker[index] += str(dater['rank']) + ' '
            valuer[index] += str(dater['value']) + ' '
        level = str(data['data']['children'][0]['stats'][0]['displayValue'])
        rank = str(data['data']['children'][0]['stats'][0]['displayRank'])
        stringtoreturn = legend_name + ' Player' + '\n\n'
        stringtoreturn += 'Level: ' + level + '\n'
        stringtoreturn += 'Player Ranking: ' + rank + '\n'
        for index, name in enumerate(namer):
            stringtoreturn += name + ': ' + valuer[index] + '             ' + 'Percentile: ' + percentiler[index] + '\n'
        #print(json.dumps(data, sort_keys=True, indent=4))
        return stringtoreturn + icon
    else:
        pass

    return ''





def celeste(channel, message, sender):
    return message[9:]

def reminder(channel, message, sender):
    return "reminder.txt for specific people maybe set timers? and it will @them reminding them like an alarmclock"
######################################END DEF METHODS#################################################


#add the "msgtotrigger": (function returning message to send), dont forget the comma!
def GetTrigger(channel, message, sender):
    triggers = {
        "!igiveup": igiveup(channel, message, sender),
        "!help": help(channel, message, sender),
        "!reminder": reminder(channel, message, sender),
        "!whoami": whoami(channel, message, sender),
        "!whoamireally": whoamireally(channel, message, sender),
        "!shellcommands": shellcommands(channel, message, sender),
        "!test": test(channel, message, sender),
        "!celeste": celeste(channel, message, sender),
        "!ddos": ddos(channel, message, sender),
        "!google": google(channel, message, sender),
        "!OCR": OCR(channel, message, sender),
        "!apex": apex(channel, message, sender)
    }
    return triggers

#####################################install additional modules#####################################
#example using pip (run once then append at top for import module-name)
#subprocess.call("#!~/Desktop/GITHUB/DiscordBot/Mainfiles/venv/Scripts \n pip install module-name", shell=true)
#added stuff
####################################################################################################
