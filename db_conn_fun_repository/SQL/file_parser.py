#import ConfigParser
import configparser
import io


# loading config file
config = configparser.ConfigParser()
config.read('config.ini')

host     = config['mysql']['host']
usr	     = config['mysql']['user']
pwd      = config['mysql']['passwd']
database = config['mysql']['db']