import urllib.request as request
import requests
import json
import ctypes
import re
import datetime
import os
import save_image


nasa_api_key="uStkwuzro4oIbu1kdJfv5s5X14HPnx42WE01QStu"
filepath ="/home/ganesh/projects/wallpapers"


def setNASAPOTD(date=None):
    #getting image url
    #getting timestamp to save as imagename
    if date is not None:
        contents = request.urlopen("https://api.nasa.gov/planetary/apod?date="+date+"&api_key="+nasa_api_key).read()
        timestamp = date
    else:
        contents = request.urlopen("https://api.nasa.gov/planetary/apod?api_key="+nasa_api_key).read()
        timestamp = save_image.getTimeStamp()
    response = json.loads(contents)
    imageurl = response['url']
    print(imageurl)

    completename = save_image.saveImage(imageurl,timestamp=timestamp)

    setWall(completename)

def setBingPOTD():
    #getting image url
    contents = request.urlopen("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US").read()
    msg=json.loads(contents)
    images = msg['images']
    images = images[0]
    data = images['url']
    print(data)

    #checking if the url contains a image and if present setting it as wall
    pattern = re.compile(r'jpg')
    if(bool(re.search(pattern,data))):

        print("image found")
        base = "http://www.bing.com"
        downurl = base + data

        completename = save_image.saveImage(downurl)

        #setting wallpaer
        setWall(completename)

#this is the main function which sets the wallpaper
def setWall(completename):
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+completename)


if __name__ == '__main__':
    potdType = input("if you wanna set nasa potd type N or if you want Bing POTD type B \n")
    if(potdType == "N" or potdType == "n"):
        setNASAPOTD()
    elif (potdType == "B" or potdType == "b"):
        setBingPOTD()
    else:
        print("invalid input try again")
