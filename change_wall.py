import sys 
import gnome as linux
import windows as windows

if (sys.platform == "linux"):
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "n":
            linux.setNASAPOTD()
        elif arg == "b":
            linux.setBingPOTD()
        else:
            linux.setBingPOTD()
    else:
        linux.setBingPOTD()
else:
    windows.setBingWallpaper()
