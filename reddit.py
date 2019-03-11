import praw
import save_image
import requests
import os

earthpornURL = "https://www.reddit.com/r/earthporn.json"

secret = "fDLs_DEOnKeYCKP5n3jJ_n5b474"
id = "sDHrovagvROA8w"
redirect = "http://webxstudio.in"

client_auth = requests.auth.HTTPBasicAuth( id , secret )

userAgent = "WallpaperBot by ganesh"

reddit = praw.Reddit(client_id = id, client_secret = secret, user_agent = userAgent)


def setWall(completename):
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+completename)

for listing in reddit.subreddit('earthporn').new(limit=1):
	completename = save_image.saveImage(listing.url)
	setWall(completename)
