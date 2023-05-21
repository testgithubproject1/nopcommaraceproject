
import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\Jyoti\\PycharmProjects\\pytest_nopcommProject\\configuration\\config.ini")

class ReadConfig():

    @staticmethod
    def geturl():
        Url=config.get('common info','Url')
        return Url

    @staticmethod
    def getemail():
        Username = config.get('common info','Email')
        return Username

    @staticmethod
    def getpassword():
        Password = config.get('common info','Password')
        return Password



