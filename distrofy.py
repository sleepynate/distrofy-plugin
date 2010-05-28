#!/usr/bin/env python
#
# (c) Nathan Dotz, 2008
# nathan.dotz@gmail.com
#
# This is distributed under the GPL v3
# Read it at http://www.fsf.org/licensing/licenses/gpl.html
#
# Distrofy 0.5 python-fu plugin for the Gimp.
# This plugin takes a picture, colors and brands it with the logos of
# popular GNU\Linux distributions. It is written half-jokingly to poke
# fun at all of the "Hot-Girl-Ubuntu-Wallpaper" that made it onto
# gnome-look.org throughout 2007-2008

from gimpfu import *
from os.path import expanduser

PATH_TO_LOGO = expanduser("~")
PATH_TO_LOGO += "/.distrofy_plugin/images/"

def _val_check(val):
    if val < -100:
        val = -100
    if val > 100:
        val = 100
    return val

def distToList(str):
    if str == 'fedora':
        distList = (210, 80, 'fedora')
    if str == 'suse':
        distList = (120, 80, 'suse')
    if str == 'mandriva':
        distList = (180, 80, 'mandriva')
    if str == 'ubuntu':
        distList = (30, 80, 'ubuntu')
    if str == 'debian':
        distList = (180, 0, 'debian')
    if str == 'slack':
        distList = (220, 20, 'slack')
    if str == 'freebsd':
        distList = (0, 80, 'freebsd')
    return distList

def distrofy( image, layer, bcOffset, bcModifier, brLightness,
                backGColor, logoPosition, distroColor):
    pdb.gimp_brightness_contrast(layer,
                                 _val_check(bcModifier-bcOffset),
                                 _val_check(bcModifier+bcOffset)
                                )
    distroColor = distToList(distroColor)
    print distroColor
    pdb.gimp_colorize(layer, distroColor[0], distroColor[1], brLightness)
    filename = distroColor[2]
    if backGColor == 'light':
        filename += "header-black.png"
    else:
        filename += "header-white.png"
    logolayer = pdb.gimp_file_load_layer(image, PATH_TO_LOGO+filename)
    pdb.gimp_image_add_layer(image, logolayer, -1)
    if logoPosition == 'upleft':
        logolayer.set_offsets(0,48)
    elif logoPosition == 'lowleft':
        logolayer.set_offsets(0, (image.height - 168) )
    elif logoPosition == 'upright':
        logolayer.set_offsets( (image.width-280) , 48)
    elif logoPosition == 'lowright':
        logolayer.set_offsets( (image.width - 280), (image.height - 168) )
    gimp.displays_flush( )

register(
    "Distrofy",
    "Distrofy v0.5",
    "Turns hot chick wallpaper into distro-branded wallpaper",
    "nathan dotz",
    "nathan dotz",
    "2008",
    "<Image>/Python-Fu/Distrofy",
    "RGB*",
    [
        (PF_SLIDER, "bcOffset", "Brightness Contrast Offset", 20, (-100, 100, 5) ),
        (PF_SLIDER, "bcModifier", "Intensity modifier", 20, (-100, 100, 5 ) ),
        (PF_SLIDER, "brLightness", "Lightness of overlay", 0 , (-100, 100, 5) ),
        (PF_RADIO, "backGColor", "Background's brightness?", "light",
            (
                ("Light", "light"),
                ("Dark", "dark")
            )
        ),
        (PF_RADIO, "logoPosition", "Logo Position?", "upleft",
            (
                ("Upper left", 'upleft'),
                ("Upper right", 'upright'),
                ("Lower left", 'lowleft'),
                ("Lower right", 'lowright')
            )
        ),
        (PF_RADIO, "distroColor", "Distro", 'ubuntu',
            (
                ("Fedora", 'fedora'),
                ("Suse", 'suse'),
                ("Mandriva", 'mandriva'),
                ("Ubuntu", 'ubuntu'),
                ("Debian", 'debian'),
                ("Slackware", 'slack'),
                ("FreeBSD", 'freebsd')
            )
        )
    ],
    [],
    distrofy)

main()
