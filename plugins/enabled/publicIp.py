from yapsy.IPlugin import IPlugin
from raspTwitter import *
import subprocess


class PublicIp(IPlugin):
    pi = ""

    def start(self, param):
        self.pi = param.pi
        for m in param.dmParsed:
        	if str(m['sender_id']) == str(param.conf['user_id']):
        		ms = m['text'].split()
        		if ((ms[0].lower() == "public") and (ms[1].lower() == "ip")):
        			self.pi.deleteDirectMessage(m['id_str'])
        			self.getPublicIp()

    def getPublicIp(self):
        p = subprocess.Popen(
            ['curl', 'ifconfig.me', '&'], stdout=subprocess.PIPE)
        ret = p.communicate()
        #print("My public IP is " + ret[0].decode('UTF-8'))
        self.pi.sendDirectMessage("My public IP is " + ret[0].decode('UTF-8'))
