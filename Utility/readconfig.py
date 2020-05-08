from configparser import ConfigParser


def readconfig(section, key):
    config1 = ConfigParser()
    config1.read("./Utility/Config.cfg")
    keyvalue=config1.get(section, key)

    return keyvalue
