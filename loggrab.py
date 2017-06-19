import os
import sys
sys.path.insert(0, os.getcwd()+"/GitterPy")
from GitterPy.gitterpy.client import GitterClient #TODO fix this for production, we go hacky for intellisense :P
#from gitterpy.client import GitterClient #IMPORTANT! uncomment this if I forgot to uncomment before pushing
from collections import OrderedDict
import json
from enum import Enum

#//configs
silent = False
room_name = "AtomicGameEngine/AtomicGameEngine"
max_messages = -1
#//we use a clash counter cause gitter isn't exactly high quality :trollface: and returns many doubles
clashes_to_abort = 5

class result(Enum):
    error=-1; clean=0; max_reached=1; has_message=2
c=0;
clashes = 0;

def grab():
    global message_id, new_messages
    global c, clashes
    while message_id is not None:
        messages_list = gtr.get('rooms/{}/chatMessages{}'.format(gtr.find_by_room_name(room_name), "?limit=100&beforeId=" + message_id))[::-1]
        message_id = None;
        for message in messages_list:
            if message['id'] in hist:
                clashes+=1
                print("clashed, total: "+str(clashes))
                if clashes >= clashes_to_abort:
                    print("hist already contains message id: "+message['id']+", html: "+message['html'])
                    return result.has_message;
            else:
                c += 1
                clashes = 0;
                if max_messages > 0:
                    if c>max_messages:
                        return result.max_reached;
                new_messages[message['id']] = {
                    'date': message['sent'],
                    'user': message['fromUser']['username'],
                    'html': message['html']
                }
                if not silent:
                    print("adding: "+message['id']+" - "+str(new_messages[message['id']]))
                message_id = message['id']
    return result.clean;

try:
    hist = OrderedDict(json.load(open("log.txt", 'r')))
    print("success loading log file")
except:
    print("error loading log file")
    hist = OrderedDict()

message_id = ""
new_messages = OrderedDict()

gtr = GitterClient(open('token.txt', 'r').readline())

print("finished with the result: "+str(grab()))

print("dumping collected data")
new_messages.update(hist)
json.dump(new_messages, open("log.txt", 'w'))

gtr.messages.send(room_name, "I just archived "+str(c)+" messages from this chat, they'll be available soon at: https://alan-fgr.github.io/AtomicGitterLog/")