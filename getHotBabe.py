#!/usr/bin/python
#
# gethotbabe.py
# Copyright 2008 Nathan Dotz nathan (dot) dotz (at) gmail (dot) com
#
# fetches a random hot babe wallpaper from http://onlysexywallpapers.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

from urllib import urlopen
from urllib import urlretrieve
from os.path import expanduser
import re

index_resource = urlopen("http://onlysexywallpapers.com")
page = index_resource.read()
page = page.replace("\n",'').replace("\t",'')
#print page + "\n\n\n"
match = re.search("Random Wallpapers</div>.*?</a>", page)
string = match.string[match.start():match.end()]
match = re.search("a href=\"/wallpaper/(.*?)/\">", string)
string = match.group(1)
#string = match.string[match.start()+8:match.end()-2]
string = "http://www.onlysexywallpapers.com/images/wmwallpapers/" + string + "-1.jpeg"
urlretrieve(string, expanduser("~")+"/.distrofy_plugin/images/distrofy.jpg")
print string
