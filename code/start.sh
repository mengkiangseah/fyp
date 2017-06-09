# !/bin/bash

# Launch monitoring server

sudo python3 ~/fyp/code/test_change_switch.py &

# Startup script for kiosk mode

export DISPLAY=:0

sudo startx /usr/bin/chromium-browser --kiosk --no-sandbox --window-size=1920,1080 --window-position=0,0 --disable-session-crashed-bubble --incognito --disable-infobars http://127.0.0.1:5000 &

echo "Done."
echo "Waiting."
sleep 10s
echo "Power stuff now."

sudo xset s off &
sudo xset -dpms &
sudo xset s noblank &
sudo xset q &

sudo unclutter &
