#!/usr/bin/python3

import os
import time
import RPi.GPIO as GPIO
import wave
import speech_recognition as sr

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
def sendToBing(filename):
	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
	    audio = r.record(source)  # read the entire audio file

	# Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
	BING_KEY = "32b3404f7cc74d34b426a360515a298b"

	try:
	    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
	except sr.UnknownValueError:
	    print("Microsoft Bing Voice Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
	return "Test file ouput. "

# Waits for the call status to change based on switch
def waitCallChange(question):
	if question == "START":
    	GPIO.wait_for_edge(27, GPIO.FALLING)
	elif question == "END":
		GPIO.wait_for_edge(27, GPIO.RISING)
	else:
		pass
	return


# Polling function to check for new files
def checkNewRecording():

	# Define path to recordings
	pathDirectory = "/var/spool/asterisk/monitor"

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
				# Check length
				audioFileIn = wave.open(addedFiles, mode='rb')

				waitCallChange("START")
				audioFileOut = wave.open(outputFile, mode= 'wb')

				# Check size
				# time.sleep(14.5)
				# Select 13.5 after pickup
				# Send query
				# Process text metric, set state
				waitCallChange("END")

			# No new files, carry one.
			else:
				pass

			# Whatever happens, update the file lists
			beforeList = afterList

		# Get ready for new call.
		setState(1)
		time.sleep(0.5)


if __name__ == '__main__':
	checkNewRecording()
