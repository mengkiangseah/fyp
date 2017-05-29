#!/usr/bin/python3

import os
import time

# Main file
def main():
    # Define path to recordings
    path_to_watch = "/var/spool/asterisk/monitor"

    # Baseline
    before = dict ([(f, None) for f in os.listdir (path_to_watch)])
    print(before)

    # Polling loop
    while 1:
        time.sleep (10)
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        if added:
            print("Added: ")
            print(added)
        before = after

if __name__ == '__main__':
    main()
