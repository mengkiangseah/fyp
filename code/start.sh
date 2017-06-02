# !/bin/bash

# Launch monitoring server

~/fyp/code/test_multithreading_server.py &

# Startup script for kiosk mode

export DISPLAY=:0

sudo startx /usr/bin/chromium-browser --kiosk --no-sandbox --window-size=5000,5000 --window-position=0,0 --disable-session-crashed-bubble --disable-infobars http://127.0.0.1:5000 &

echo "Done."
echo "Waiting."
sleep 10s
echo "Power stuff now."

sudo xset s off &
sudo xset -dpms &
sudo xset s noblank &
sudo xset q &

sudo unclutter &
