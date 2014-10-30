from yapsy.IPlugin import IPlugin
from raspTwitter import *
import subprocess


class Reboot(IPlugin):
    pi = ""

    def start(self, param):      
        self.pi = param.pi
        for m in param.dmParsed:
          if str(m['sender_id']) == str(param.conf['user_id']):
            ms = m['text'].split()
            if (ms[0].lower() == "reboot"):
                self.pi.deleteDirectMessage(m['id_str'])
                self.rebootPi()
                    

    def rebootPi(self):
        p = subprocess.Popen(["sudo", "reboot"], stdout=subprocess.PIPE)
        ret = p.communicate()
        self.pi.sendDirectMessage(ret[0].decode('UTF-8'))