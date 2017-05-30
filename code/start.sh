# !/bin/bash

# Startup script for kiosk mode

echo "Script running..."

xset s off
xset -dpms
xset s noblank

echo "Screensavers and screen blanking removed."

unclutter &

echo "Unclutter to remove mouse pointer done."

startx /usr/bin/chromium-browser --kiosk --no-sandbox -- window-size=1280,1024 --window-position=0,0 --disable-session-crashed-bubble --disable-infobars file:/// &
