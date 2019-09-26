#!/home/kwazinator/PycharmProjects/robits/venv/bin/python3.5
import discord
import trigger
from importlib import reload
import FenoxWordcloud
from google_images_download import google_images_download
from PIL import Image
import os
import subprocess
import time
import db
import plotlypackage

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji)
        print(reaction.emoji.id)
        print(user)

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        utf8message = '{0.content}'.format(message)
        sender = '{0.author}'.format(message)
        #load text for each channel
        if sender != 'Kahzam#8492':
            filename = "Fenox" + str(message.channel) + '.txt'
            if utf8message[0] != '!':
                with open(filename,'a') as myfile:
                    myfile.write(utf8message + '\n')

            #reload for gitpushes
            t = reload(trigger)


            checkmessage = utf8message.split(' ')[0]
            trig = t.GetTrigger(str(message.channel), utf8message,sender)
            if checkmessage in trig:
                msg = trig.get(checkmessage, "")
            elif utf8message[0] == '!':
                msg = "invalid command please use !help for help"
            else:
                msg = ''
            #print(msg)
            if checkmessage == "!google":
                response = google_images_download.googleimagesdownload() #limit is number of images to put in
                arguments = {"keywords": utf8message[7:], "limit": 3, "print_urls": True}
                paths = response.download(arguments)
                print(paths)
                paths = paths[0][utf8message[7:]]
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
                newimage = '/opt/DiscordBot/Mainfiles/downloads/' + utf8message[8:] + '.jpg'
                new_im.save(newimage, "JPEG")
                await message.channel.send(file=discord.File(fp=newimage, filename=(utf8message[8:]+'.jpg')))
            elif utf8message == "!wordcloud":
                FenoxWordcloud.dochannel(filename)
                picture = filename + '.png'
                await message.channel.send(file=discord.File(fp=picture, filename=(picture + '.png')))
            elif checkmessage == "!del":
                if (sender == 'Svlad_Cjelli#0042' or sender =='chan2#2445'):
                    try:
                        mgs = [] #Empty list to put all the messages in the log
                        number = int(utf8message[5:]) + 1
                        async for x in message.channel.history(limit = number):
                            await x.delete()
                    except Exception as e:
                        msg = e
                    finally:
                        pass
                else:
                    msg = 'You do not have sufficient permissions to delete messages'
            elif checkmessage == '!root':
                if (sender == 'chan2#2445'):
                    try:
                        syscall = utf8message[6:].split(' ')
                        msg = subprocess.check_output(syscall)
                    except Exception as e:
                        msg = e
                    finally:
                        pass
            elif checkmessage =='!reload':
                if (sender == 'Svlad_Cjelli#0042' or sender == 'chan2#2445'):
                    try:
                        os.execl('./discordbot.py','')
                    except Exception as e:
                        msg = e
                    finally:
                        pass
            elif checkmessage == '!^^^':
                try:
                    mgs = [] #Empty list to put all the messages in the log
                    async for x in message.channel.history(limit = 2):
                        mgs.append(x)
                    #await client.delete_messages(mgs[0])
                    await mgs[0].delete()
                    await mgs[1].add_reaction('b_U:534863131978104853')
                    await mgs[1].add_reaction('g_U:534863064487428106')
                    await mgs[1].add_reaction('r_U:534827521925971987')
                    await mgs[1].add_reaction('y_U:534863097417039902')
                except Exception as e:
                    msg = e
                finally:
                    pass
            if msg != "":
                await message.channel.send(msg)
            if checkmessage =='!terraria-reset':
                try:
                    subprocess.call('screen -S terraria -X stuff \'exit-nosave\'$(echo -ne \'\\015\')', shell=True)
                    time.sleep(10)
                    await message.channel.send('exited and saved world')
                    subprocess.call('screen -S terraria -X stuff \'./tModLoaderServer\'$(echo -ne \'\\015\')', shell=True)
                    time.sleep(25)
                    await message.channel.send('starting tModLoaderServer')
                    subprocess.call('screen -S terraria -X stuff \'2\'$(echo -ne \'\\015\')', shell=True)
                    time.sleep(1)
                    subprocess.call('screen -S terraria -X stuff \'\'$(echo -ne \'\\015\')', shell=True)
                    time.sleep(1)
                    subprocess.call('screen -S terraria -X stuff \'7778\'$(echo -ne \'\\015\')', shell=True)
                    time.sleep(1)
                    subprocess.call('screen -S terraria -X stuff \'n\'$(echo -ne \'\\015\')', shell=True)
                    time.sleep(1)
                    subprocess.call('screen -S terraria -X stuff \'\'$(echo -ne \'\\015\')', shell=True)
                    await message.channel.send('starting World MinecraftRulez')
                    time.sleep(30)
                    await message.channel.send('World MinecraftRulez Up')
                except Exception as e:
                    await message.channel.send(str(e))
                finally:
                    pass
            elif checkmessage =='!terraria-night':
                subprocess.call('screen -S terraria -X stuff \'dusk\'$(echo -ne \'\\015\')', shell=True)
            elif checkmessage == '!terraria-day':
                subprocess.call('screen -S terraria -X stuff \'noon\'$(echo -ne \'\\015\')', shell=True)
            elif checkmessage =='!terraria-save':
                subprocess.call('screen -S terraria -X stuff \'save\'$(echo -ne \'\\015\')', shell=True)
                time.sleep(6)
                await message.channel.send('World Saved Successfuly')
            elif checkmessage =='!poll':
                plotlypackage.makeimage().save('/opt/DiscordBot/Mainfiles/test.png',"png")
                await message.channel.send(file=discord.File(fp='/opt/DiscordBot/Mainfiles/test.png', filename=('test' + '.png')),content='test')



client = MyClient()
with open('clientid.dat','r') as myfile:
    OauthToken = myfile.read()
client.run(str(OauthToken[:-1]))
