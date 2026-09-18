import configparser
import os.path


#ConfigParser is a Python class that understands .ini files
# __file__is a special Python variable. It represents the path of the current Python file
#@classmethod means the method belongs to the class itself, rather than a particular object/instance.So we can call it directly

class Configreader:
    config = configparser.ConfigParser()

    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config","config.ini")
    config.read(config_path)

    @classmethod
    def get_browser(cls):
        return cls.config.get("environment","browser")

    @classmethod
    def get_base_url(cls):
        return cls.config.get("environment","base_url")

    @classmethod
    def get_timeout(cls):
        return cls.config.get("environment","timeout")