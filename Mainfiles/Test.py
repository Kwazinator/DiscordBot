#!/usr/bin/env python
#-*- coding:utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import urllib.parse
import git

HOST_NAME = '0.0.0.0'
PORT_NUMBER = 9000


def handle_hook(payload):
    if 'Mainfiles/' in payload and "modified" in payload and 'DiscordBot' in payload:
        g = git.cmd.Git('~/Desktop/GITHUB/DiscordBot/Mainfiles')
        g.pull()


class HookHandler(BaseHTTPRequestHandler):
    server_version = "HookHandler/0.1"
    def do_GET(s):
        s.send_response(200)
        s.wfile.write('Hello!')

    def do_POST(s):
        # Check that the IP is within the GH ranges
        if not any(s.client_address[0].startswith(IP)
                   for IP in ('192.30.252', '192.30.253', '192.30.254', '192.30.255')):
            s.send_error(403)

        length = int(s.headers['Content-Length'])
        post_data = urllib.parse.parse_qs(s.rfile.read(length).decode('utf-8'))
        #payload = json.loads(post_data['commits'])
        handle_hook(str(post_data))

        s.send_response(200)



if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), HookHandler)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))