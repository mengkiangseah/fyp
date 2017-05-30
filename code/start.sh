# !/bin/bash

# Startup script for kiosk mode

sudo startx /usr/bin/chromium-browser --kiosk --no-sandbox --window-size=1280,1024 --window-position=0,0 --disable-session-crashed-bubble --disable-infobars file:///

xset s off
xset -dpms
xset s noblank

unclutter &

