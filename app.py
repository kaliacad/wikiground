from gi.repository import Gio
import os

file_location = os.getcwd() + "/images/bkg.jpg"
uri = 'file://%s' % file_location

SCHEMA = "org.gnome.desktop.background"
KEY = "picture-uri"
gsettings = Gio.Settings.new(SCHEMA)
gsettings.set_string(KEY, uri)

# TODO
# Load images from Wikimedia commons 1/day
# Store images localy
# Set background randomly
# Make the program works for Windows
# Automate the whole process

gsettings.apply()
