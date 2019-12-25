#!/home/kwaz/flaskapp/flaskappenv/bin/python3.6
from flask import Flask, request
import json
import git
import subprocess

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
   data = json.loads(request.data)
   #print("New commit by: {}".format(data['commits'][0]['author']['name']))
   if data['data'] == 'backup':
       subprocess.call('screen -S minecraft -X stuff \'backup start\'$(echo -ne \'\\015\')', shell=True)
       return "OK"
   elif data['data'] == 'stop':
       subprocess.call('screen -S minecraft -X stuff \'stop\'$(echo -ne \'\\015\')', shell=True)
       return "OK"
   elif data['data'] == 'start':
       subprocess.call('screen -S minecraft -X stuff \'./run.sh\'$(echo -ne \'\\015\')', shell=True)
       return "OK"
   elif data['data'] == 'status':
       subprocess.call('screen -S minecraft -X stuff \'backup start\'$(echo -ne \'\\015\')', shell=True)
       return "OK"
if __name__ == '__main__':
   app.run(host='0.0.0.0',port='7676')

