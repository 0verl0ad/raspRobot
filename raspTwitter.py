from twitter import *


class RaspTwitter:

    """A class to interact with twitter"""
    t = ""
    conf = {}

    def __init__(self, param):
        self.conf = param.conf
        self.t = Twitter(auth=OAuth(self.conf['token'],
                                    self.conf['token_key'],
                                    self.conf['con_secret'],
                                    self.conf['con_secret_key'])
                         )

    def postTweet(self, msg):
        self.t.statuses.oembed(_id=1234567890)
        self.t.statuses.update(status=msg)

    def getDirectMessages(self):
        return self.t.direct_messages()

    def parseDirectMessages(self, dmList):
        mList = []
        for dm in dmList:
            m = {}
            m['id_str'] = dm['id_str']
            m['sender_screen_name'] = dm['sender_screen_name']
            m['sender_id'] = dm['sender_id']
            m['text'] = dm['text']
            mList.append(m)
            # self.deleteDirectMessage(dm['id_str'])
        return mList

    def getDirectMessage(self, msgId):
        return self.t.direct_messages.show(id=msgId)

    def deleteDirectMessage(self, msgId):
        return self.t.direct_messages.destroy(id=msgId)

    def sendDirectMessage(self, msgText):
        return self.t.direct_messages.new(
            user=self.conf['userName'], text=msgText)
