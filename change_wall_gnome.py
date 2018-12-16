import urllib.request as request
import requests
import json
import ctypes
import re
import datetime
import os


nasa_api_key="uStkwuzro4oIbu1kdJfv5s5X14HPnx42WE01QStu"
filepath ="/home/ganesh/projects/wallpapers"


def setNASAPOTD(nasa_api_key,date=None):
    #getting image url
    #getting timestamp to save as imagename
    if date is not None:
        contents = request.urlopen("https://api.nasa.gov/planetary/apod?date="+date+"&api_key="+nasa_api_key).read()
        timestamp = date
    else:
        contents = request.urlopen("https://api.nasa.gov/planetary/apod?api_key="+nasa_api_key).read()
        timestamp = getTimeStamp()
    response = json.loads(contents)
    imageurl = response['url']
    print(imageurl)

    #defining place where the wallpaper will be stored
    results=requests.get(imageurl)
    completename=os.path.join(filepath,"Nasa_"+timestamp+".jpg")
    open(completename,'wb').write(results.content)
    setWall(completename)

def setBingPOTD():
    #getting image url
    contents = request.urlopen("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US").read()
    msg=json.loads(contents)
    images = msg['images']
    images = images[0]
    data = images['url']
    print(data)

    #getting timestamp to save as imagename
    timestamp = getTimeStamp()

    #checking if the url contains a image and if present setting it as wall
    pattern = re.compile(r'jpg')
    if(bool(re.search(pattern,data))):

        print("image found")
        base = "http://www.bing.com"
        downurl = base + data

        #defining place where the wallpaper will be stored
        results=requests.get(downurl)
        completename=os.path.join(filepath,"Bing_"+timestamp+".jpg")
        open(completename,'wb').write(results.content)

        #setting wallpaer
        setWall(completename)

#this is the main function which sets the wallpaper
def setWall(completename):
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+completename)


def getTimeStamp():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d")
    return timestamp

potdType = input("if you wanna set nasa potd type N or if you want Bing POTD type B")
if(potdType == "N" or potdType == "n"):
    setNASAPOTD(nasa_api_key)
elif (potdType == "B" or potdType == "b"):
    setBingPOTD()
else:
    print("invalid input try again")