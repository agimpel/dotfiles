#!/bin/sh

player_status=$(playerctl -p spotify status)

if [ "$player_status" = "Playing" ]; then
    echo "$(playerctl -p spotify metadata title)  -  $(playerctl -p spotify metadata artist)"
elif [ "$player_status" = "Paused" ]; then
    echo ""
else
    echo ""
fi
