#!/bin/bash

screencapture -i /tmp/snapshot.png
curl http://localhost:8080/upload -F "file=@/tmp/snapshot.png" | grep -Eo '"markdown": "([^"]*)"' | grep -Eo '![^"]*' | pbcopy
