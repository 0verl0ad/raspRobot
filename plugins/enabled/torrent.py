from yapsy.IPlugin import IPlugin
from raspTwitter import *
import urllib.request


class Torrent(IPlugin):
    pi = ""
    conf = {}

    def start(self, param):
        self.pi = param.pi
        self.conf = param.conf
        for m in param.dmParsed:
            if str(m['sender_id']) == str(param.conf['user_id']):
                ms = m['text'].split()
                if (ms[0].lower() == "torrent"):
                    self.pi.deleteDirectMessage(m['id_str'])
                    self.downloadTorrent(ms[1].lower())

    def downloadTorrent(self, torrentUrl):
        torrentUrl = torrentUrl.replace("///", "//");
        pos = torrentUrl.rfind('/')
        torrentName = torrentUrl[pos+1:]
        saveAs = self.conf['torrentsDir'] + '/' + torrentName
        urllib.request.urlretrieve(torrentUrl, saveAs)
        self.pi.sendDirectMessage("Downloading torrent file -> " + torrentName)
