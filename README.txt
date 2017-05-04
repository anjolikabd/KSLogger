Hello! 

KeyScreenLogger is a tool which records keystrokes and takes screenshots on a user's computer and sends the logged data to Dropbox. 

***Must Enable Terminal to make changes on computer by going to System Preferences > Security and Privacy > Accessibility  and add Terminal to apps allowed to control your computer***

Usage:

Run
> python main.py

Happy logging!


For the purposes of demonstrating its functionality I have set up a Dropbox account. If you want to use your own Dropbox account to upload the logged data, do the following:

- Log into your Dropbox account
- Go to https://www.dropbox.com/developers/apps
- Create a new app, select Dropbox API
- On the next page Generate Access Token 
- In keylogger.cfg change the username, password, and access token under the DBInfo section

- You can also modify the runtime of the tool as well as the directories where you want to direct the data to
- Default runtime is 1 minute

Dependencies:

You will need to have Python installed

Modules:
- sys
- os
- Foundation 
- Cocoa 

- AppKit
- PyObjCTools
- time
- configparser
- dropbox
- datetime
