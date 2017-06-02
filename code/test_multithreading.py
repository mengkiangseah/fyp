#!/usr/bin/python3

import threading
import time

global keypress

keypress = 0

def increment():
    global keypress
    while(True):
        print("Incrementing keypress.")
        keypress = keypress + 1
        time.sleep(2)


def main():
    global keypress
    while(True):
        print("Keypress value is: " + str(keypress))
        time.sleep(1)

if __name__ == '__main__':
    thread1 = threading.Thread(target=increment)
    thread2 = threading.Thread(target=main)
    print("Running one.")
    thread1.start();
    print("Running two.")
    thread2.start();
