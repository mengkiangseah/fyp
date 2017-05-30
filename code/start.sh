# !/bin/bash

# Startup script for kiosk mode

export DISPLAY=:0

sudo startx /usr/bin/chromium-browser --kiosk --no-sandbox --window-size=5000,5000 --window-position=0,0 --disable-session-crashed-bubble --disable-infobars file:/// &

sudo xset q & 
sudo xset s off &
sudo xset -dpms &
sudo xset s noblank &

sudo unclutter &

