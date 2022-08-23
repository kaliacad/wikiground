from gi.repository import Gio
import os
from sys import argv

SCHEMA = "org.gnome.desktop.background"
KEY = "picture-uri"

gsettings = Gio.Settings.new(SCHEMA)

def get_wallpaper():
    print(gsettings.get_string("picture-uri"))

def set_wallpaper(image_path):
    uri = 'file://%s' % image_path
    gsettings.set_string(KEY, uri)

def is_argument_free():
    return len(argv) == 1

if (is_argument_free() == True):
    get_wallpaper()
else:
    image_path = argv[1]
    set_wallpaper(image_path)

# TODO
# Load images from Wikimedia commons 1/day
# Store images localy
# Set background randomly
# Make the program works for Windows
# Automate the whole process
# Apply background color if supplied
