#!/bin/bash

gnome-screenshot -a -c
xclip -selection clipboard -t image/png -o > /tmp/snapshot.png
curl http://localhost:8080/upload -F "file=@/tmp/snapshot.png" | grep -Po '"url": "([^"]*)"' | grep -Po 'http[^"]*' | xclip -selection clipboard
