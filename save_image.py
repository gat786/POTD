import requests
import os
import getpass
import datetime

#defining place where the wallpaper will be stored
filepath = os.getcwd()

def saveImage(downurl,timestamp=None):
    results=requests.get(downurl)
    timestamp = timestamp if (timestamp!=None) else getTimeStamp()
    walls_dir = os.path.join(filepath,"wallpapers")
    print(walls_dir)
    if os.path.exists(walls_dir)!=True:
        os.makedirs(walls_dir)
    completename=os.path.join(walls_dir,"Image_"+timestamp+".jpg")
    open(completename,'wb').write(results.content)
    return completename

def getTimeStamp():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d-%H%M%S")
    return timestamp
