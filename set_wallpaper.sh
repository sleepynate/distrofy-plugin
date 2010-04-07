#!/bin/bash
BACKS="$HOME/.distrofy_plugin/images/distrofy.jpg" ;
#gconftool-2 -t str --set /desktop/gnome/background/picture_filename "$BACKS" ;
#gconftool-2 -t str --set /desktop/gnome/background/picture_options "stretched" ;
feh --bg-scale $BACKS
