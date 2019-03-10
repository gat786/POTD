import urllib.request as request
import json
import ctypes
import re
import datetime
import os

def setBingWallpaper():
    contents = request.urlopen("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US").read()

    msg=json.loads(contents)

    images = msg['images']

    images = images[0]

    data = images['url']

    print(data)

    now = datetime.datetime.now()

    timestamp = now.strftime("%Y-%m-%d")

    print(timestamp)

    pattern = re.compile(r'jpg')
    if(bool(re.search(pattern,data))):

        print("image found")
        
        base = "http://www.bing.com"

        downurl = base + data

        filename ="C:\\flutter\\wallpaper\\download-"+timestamp+".jpg"

        request.urlretrieve(downurl,filename)

        pathToBmp = os.path.normpath(filename)

        ctypes.windll.user32.SystemParametersInfoW(20, 0, pathToBmp , 3)
