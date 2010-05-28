#!/usr/bin/env python
#
# (c) Nathan Dotz, 2008
# nathan (dot) dotz (at) gmail (dot) com
#
# This is distributed under the GPL v3
# Read it at http://www.fsf.org/licensing/licenses/gpl.html
#
# ALWAYS RUN NON-INTERACTIVE

from gimpfu import *
from os.path import expanduser

PATH_TO_LOGO = expanduser("~")
PATH_TO_LOGO += "/.distrofy_plugin/images/"


def batchDistrofy(distroToUse):
    print "Starting Distrofication Process ... "
    dimage = pdb.file_jpeg_load(PATH_TO_LOGO+"distrofy.jpg", PATH_TO_LOGO+"distrofy.jpg")
    ddrawable = pdb.gimp_image_get_active_layer(dimage)
    mean, std_dev, median, pixels, count, percentile = pdb.gimp_histogram(ddrawable, 0, 0, 255)
    if median > 50:
        passcolor = 'light'
    else:
        passcolor = 'dark'
    print "Image loaded"
    pdb.python_fu_Distrofy(dimage, ddrawable, 20, 20, 0, passcolor, "topleft", distroToUse)
    print "Filter Applied"
    pdb.gimp_image_get_active_layer(dimage).set_offsets(0,48)
    ddrawable = pdb.gimp_image_flatten(dimage)
    print "Image Flattened"
    pdb.file_jpeg_save(dimage, ddrawable,
        PATH_TO_LOGO+"distrofy.jpg", PATH_TO_LOGO+"distrofy.jpg",
        0.85, 0, 1, 0, "Made with the Distrofy Gimp Plug-in, by Nathan Dotz",
        3, 1, 0, 1)

register(
    "batchDistrofy",
    "Batch Processor for Distrofy",
    "Batch Processor for Distrofy Plugin",
    "nathan dotz",
    "nathan dotz",
    "2008",
    "",
    "RGB*",
    [ (PF_STRING, "distroToUse", "Distribution to apply to image", "slack") ],
    [],
    batchDistrofy)

main()
