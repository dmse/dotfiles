#!/bin/bash

sleep 0.1 && scrot -s '/tmp/scrot-%Y%m%d-%H%M%S.png' -e 'xclip -selection c -target image/png -i $f' 2>~/.scrot.log; notify-send 'scrot+xclip' 'Screenshot copied to clipboard.'
