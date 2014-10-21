from yapsy.PluginManager import PluginManager
from parameters import *
from raspTwitter import *
#from time import sleep
import time


def parseConfigFile(fileName):
    conf = {}
    f = open(fileName, 'r')
    for l in f.readlines():
        ls = l.split()
        if ls and ('#' not in ls[0]):
            conf[ls[0]] = ls[2]
    f.close()
    return conf


def main():
    configFile = 'config'
    
    param = Parameters()
    param.conf = parseConfigFile(configFile)
    param.pi = RaspTwitter(param)
    
    while True:      
        print(time.ctime())
        param.dm = param.pi.getDirectMessages()
        param.dmParsed = param.pi.parseDirectMessages(param.dm)
    
        # Load the plugins from the plugin directory.
        manager = PluginManager()
        manager.setPluginPlaces(["plugins/enabled"])
        manager.collectPlugins()

        for plugin in manager.getAllPlugins():
            plugin.plugin_object.start(param)

        time.sleep(60)


if __name__ == '__main__':
    main()
