import sys 
import change_wall_gnome as linux
import change_wall_windows as windows

if (sys.platform == "linux"):
    arg = sys.argv[1]
    if arg == "n":
        linux.setNASAPOTD()
    elif arg == "b":
        linux.setBingPOTD()
    else:
        linux.setBingPOTD()
else:
    windows.setBingWallpaper()