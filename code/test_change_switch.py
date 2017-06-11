#!/usr/bin/python3

import os
import time
import RPi.GPIO as GPIO
import wave
import speech_recognition as sr
from flask import Flask, render_template
import threading

# Server object
app = Flask(__name__)

# Overall system state
global state
state = 1

# Set up switch input
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# Setting to set state, removes need to declare global each time.
def setState(newState):
	global state
	state = newState
	print("State set to: " + str(state) + ". ")
	return

# List Directory Function
def listDirectory(pathDirectory):
	outputList = []

	for root, dirs, files in os.walk(pathDirectory, topdown=False):
		for name in files:
			outputList.append(os.path.join(root, name))
		for name in dirs:
			outputList.append(os.path.join(root, name))
	return outputList

# Send to Bing
def sendToBing():
	r = sr.Recognizer()
	with sr.AudioFile("/home/pi/outputFile.wav") as source:
		audio = r.record(source)  # read the entire audio file

	# Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
	BING_KEY = "32b3404f7cc74d34b426a360515a298b"

	try:
		detectedSpeech = r.recognize_bing(audio, key=BING_KEY)
	except sr.UnknownValueError:
		detectedSpeech = "Microsoft Bing Voice Recognition could not understand audio."
	except sr.RequestError as e:
		detectedSpeech = "Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e)

	print("Here is the output.")
	print(detectedSpeech)
	return detectedSpeech

# Waits for the call status to change based on switch
def waitCallChange(question):
	if question == "START":
		GPIO.wait_for_edge(27, GPIO.FALLING)
	elif question == "END":
		GPIO.wait_for_edge(27, GPIO.RISING)
	else:
		pass
	return

# Call danger metric
def callMetric(wordsSpoken):
	return 4


# Polling function to check for new files
def checkNewRecording():
	# Length of analysed audio
	lengthAudio = 14

	# Define path to recordings and output
	pathDirectory = "/var/spool/asterisk/monitor"
	outputFile = "/home/pi/outputFile.wav"

	# Baseline
	beforeList = listDirectory(pathDirectory)

	# Polling loop
	while True:
		# Call without recording is a known caller
		if GPIO.input(27) == GPIO.LOW:
			# Set state, wait for call to end.
			setState(2)
			waitCallChange("END")

		# Otherwise, check for change in files
		else:
			afterList = listDirectory(pathDirectory)
			addedFiles = [f for f in afterList if (not f in beforeList and ".wav" in f)]

			# New file found, call is therefore incoming.
			if addedFiles:
				setState(3)
				# Open recording
				print(addedFiles[0])
				audioFileIn = open(addedFiles[0], mode='rb')

				# Wait for call to start, then file size of file.
				waitCallChange("START")
				audioFileInSize = os.path.getsize(addedFiles[0])

				# Wait for data to collect
				time.sleep(lengthAudio + 0.5)

				# Prepare file to be sent. Open output file, select data from recording, write.
				audioFileOut = wave.open(outputFile, mode= 'wb')
				audioFileOut.setparams((1, 2, 8000, 8000 * lengthAudio, 'NONE', 'not compressed'))
				audioFileIn.seek(audioFileInSize)
				audioFileOut.writeframes(audioFileIn.read(2 * 8000 * lengthAudio))

				# Process text metric, set state
				spokenText = sendToBing()
				setState(callMetric(spokenText))

				# Wait for call end
				waitCallChange("END")

			# No new files, carry one.
			else:
				pass

			# Whatever happens, update the file lists
			beforeList = afterList

		# Get ready for new call.
		setState(1)
		time.sleep(0.5)

# Servers
@app.route("/")
def index():
	global state
	return render_template('index.html', the_state=state)

def serverFunction():
	app.run()

if __name__ == "__main__":
	analysisThread = threading.Thread(target=checkNewRecording)
	serverThread = threading.Thread(target=serverFunction)
	print("Running analysisThread.")
	analysisThread.start();
	print("Running serverThread.")
	serverThread.start();
