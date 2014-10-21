from yapsy.IPlugin import IPlugin
from raspTwitter import *
import subprocess


class Ssh(IPlugin):
	pi = ""

	def start(self, param):  	
		self.pi = param.pi
		for m in param.dmParsed:
			if str(m['sender_id']) == str(param.conf['user_id']):
				ms = m['text'].split()
				if ((ms[0].lower() == "ssh") and ((ms[1].lower() == "on") or (ms[1].lower() == "start"))):
					self.pi.deleteDirectMessage(m['id_str'])
					self.startSsh()
				elif ((ms[0].lower() == "ssh") and ((ms[1].lower() == "off") or (ms[1].lower() == "stop"))):
					self.pi.deleteDirectMessage(m['id_str'])
					self.stopSsh()
				elif ((ms[0].lower() == "ssh") and (ms[1].lower() == "status")):
					self.pi.deleteDirectMessage(m['id_str'])
					self.statusSsh()
					

	def statusSsh(self):
		p = subprocess.Popen(["sudo", "service", "ssh", "status"], stdout=subprocess.PIPE)
		ret = p.communicate()
		self.pi.sendDirectMessage(ret[0].decode('UTF-8'))

	def startSsh(self):
		p = subprocess.Popen(["sudo", "service", "ssh", "start"], stdout=subprocess.PIPE)
		ret = p.communicate()
		self.pi.sendDirectMessage(ret[0].decode('UTF-8'))

	def stopSsh(self):
		p = subprocess.Popen(["sudo", "service", "ssh", "stop"], stdout=subprocess.PIPE)
		ret = p.communicate()
		self.pi.sendDirectMessage(ret[0].decode('UTF-8'))