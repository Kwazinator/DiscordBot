#!/home/kwazinator/PycharmProjects/robits/venv/bin/python3.5
import discord
import trigger
from importlib import reload
import FenoxWordcloud
from google_images_download import google_images_download
from PIL import Image
import sys

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        utf8message = '{0.content}'.format(message)
        sender = '{0.author}'.format(message)
        #load text for each channel
        filename = "Fenox" + str(message.channel) + '.txt'
        with open(filename,'a') as myfile:
            myfile.write(utf8message + '\n')

        #reload for gitpushes
        t = reload(trigger)


        checkmessage = utf8message.split(' ')[0]
        trig = t.GetTrigger(str(message.channel), utf8message,sender)
        if checkmessage in trig:
            msg = trig.get(checkmessage, "")
        else:
            msg = ""
        #print(msg)
        if checkmessage == "!google":
            response = google_images_download.googleimagesdownload() #limit is number of images to put in
            arguments = {"keywords": utf8message[7:], "limit": 3, "print_urls": True}
            paths = response.download(arguments)
            paths = paths[utf8message[7:]]
            images = map(Image.open, paths)
            widths, heights = zip(*(i.size for i in images))
            images = map(Image.open, paths) #apparently maps can only be iterated over once
            total_width = sum(widths)
            max_height = max(heights)

            new_im = Image.new('RGB', (total_width, max_height))

            x_offset = 0
            for im in images:
                new_im.paste(im, (x_offset,0))
                x_offset += im.size[0]
            newimage = '/home/kwazinator/Desktop/GITHUB/DiscordBot/Mainfiles/downloads/' + utf8message[8:] + '.jpg'
            new_im.save(newimage, "JPEG")
            with open(newimage, 'rb') as picture:
                await client.send_file(message.channel, picture)

        elif utf8message == "!wordcloud":
            FenoxWordcloud.dochannel(filename)
            picture = filename + '.png'
            with open(picture, 'rb') as picture:
                await client.send_file(message.channel, picture)
        if msg != "":
            await client.send_message(message.channel, msg)

client = MyClient()
with open('clientid.dat','r') as myfile:
    OauthToken = myfile.read()
client.run(str(OauthToken[:-1]))
