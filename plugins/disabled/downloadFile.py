from yapsy.IPlugin import IPlugin
from raspTwitter import *
import subprocess


class DownloadFile(IPlugin):
    pi = ""
    conf = {}

    def start(self, param):
        self.pi = param.pi
        self.conf = param.conf
        for m in param.dmParsed:
            if str(m['sender_id']) == str(param.conf['user_id']):
                ms = m['text'].split()
                if (ms[0].lower() == "download"):
                    self.pi.deleteDirectMessage(m['id_str'])
                    self.DownloadF(ms[1].lower())

    def DownloadF(self, fileUrl):
        fileUrl = fileUrl.replace("///", "//");
        pos = fileUrl.rfind('/')
        fileName = fileUrl[pos+1:]
        saveAs = self.conf['downloadsDir'] + '/' + fileName
        urllib.request.urlretrieve(fileUrl, saveAs)
        self.pi.sendDirectMessage("Downloading file -> " + fileName)
