from yapsy.IPlugin import IPlugin
from raspTwitter import *
import subprocess


class Services(IPlugin):
    pi = ""

    def start(self, param):
        self.pi = param.pi
        for m in param.dmParsed:
            if str(m['sender_id']) == str(param.conf['user_id']):
                ms = m['text'].split()
                if ((ms[0].lower() == "service") and (ms[2].lower() == "start")):
                    self.pi.deleteDirectMessage(m['id_str'])
                    self.startService(ms[1].lower())
                elif ((ms[0].lower() == "service") and (ms[2].lower() == "stop")):
                    self.pi.deleteDirectMessage(m['id_str'])
                    self.stopService(ms[1].lower())
                elif ((ms[0].lower() == "service") and (ms[2].lower() == "status")):
                    self.pi.deleteDirectMessage(m['id_str'])
                    self.statusService(ms[1].lower())
                elif ((ms[0].lower() == "service") and (ms[2].lower() == "restart")):
                    self.pi.deleteDirectMessage(m['id_str'])
                    self.statusService(ms[1].lower())
                    

    def statusService(self, serviceName):
        p = subprocess.Popen(["sudo", "service", serviceName, "status"], stdout=subprocess.PIPE)
        ret = p.communicate()
        self.pi.sendDirectMessage(ret[0].decode('UTF-8'))

    def startService(self, serviceName):
        p = subprocess.Popen(["sudo", "service", serviceName, "start"], stdout=subprocess.PIPE)
        ret = p.communicate()
        self.pi.sendDirectMessage(ret[0].decode('UTF-8'))

    def stopService(self, serviceName):
        p = subprocess.Popen(["sudo", "service", serviceName, "stop"], stdout=subprocess.PIPE)
        ret = p.communicate()
        self.pi.sendDirectMessage(ret[0].decode('UTF-8'))

    def restartService(self, serviceName):
        p = subprocess.Popen(["sudo", "service", serviceName, "restart"], stdout=subprocess.PIPE)
        ret = p.communicate()
        self.pi.sendDirectMessage(ret[0].decode('UTF-8'))