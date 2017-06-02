#!/usr/bin/python3

from flask import Flask, render_template
import threading
import time

app = Flask(__name__)

global state
state = 0

@app.route("/")
def index():
    global state
    return render_template('index.html', the_state=state)

def serverFunction():
    app.run()

def incrementFunction():
    global state
    while(True):
        state = state + 1
        time.sleep(7)


if __name__ == "__main__":
    incrementThread = threading.Thread(target=incrementFunction)
    serverThread = threading.Thread(target=serverFunction)

    print("Running incrementThread.")
    incrementThread.start();
    print("Running serverThread.")
    serverThread.start();
