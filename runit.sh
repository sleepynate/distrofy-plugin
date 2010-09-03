#!/bin/bash
#
# (c) Nathan Dotz, 2008
# nathan (dot) dotz (at) gmail (dot) com
#
# This is distributed under the GPL v3
# Read it at http://www.fsf.org/licensing/licenses/gpl.html
#
~/.distrofy_plugin/getHotBabe.py
gimp -i --no-data --no-fonts -b '(python-fu-batchDistrofy 1 fedora)' -b  '(gimp-quit 0)'
~/.distrofy_plugin/set_wallpaper.sh
