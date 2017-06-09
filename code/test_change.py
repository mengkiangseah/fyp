#!/usr/bin/python3

import os
import time
import wave

# Main file
def directory_listing(path_to_watch):
	the_output = []

	for root, dirs, files in os.walk(path_to_watch, topdown=False):
		for name in files:
			the_output.append(os.path.join(root, name))
		for name in dirs:
			the_output.append(os.path.join(root, name))
	return the_output

def main():
	# Define path to recordings
	path_to_watch = "/var/spool/asterisk/monitor"

	# Baseline
	before = directory_listing(path_to_watch)
	print(before)

	# Polling loop
	while True:
		time.sleep (10)
		after = directory_listing(path_to_watch)

		added = [f for f in after if (not f in before and ".wav" in f)]

		# New file found, call is therefore incoming.
		if added:
			# Open recording
			print(added[0])
			audioFileIn = wave.open(addedFiles[0], mode='rb')

			oldsizeData = audioFileIn.getnframes()

			# Wait for data to collect
			time.sleep(lengthAudio + 0.5)

			# Prepare file to be sent. Open output file, select data from recording, write.
			audioFileOut = wave.open("/home/pi/output.wav", mode= 'wb')
			audioFileOut.setparams((1, 2, 8000, 8000 * lengthAudio, 'NONE', 'not compressed'))
			audioFileIn.readframes(oldsizeData)
			audioFileOut.writeframes(audioFileIn.readframes(8000 * lengthAudio))

		before = after

if __name__ == '__main__':
	main()
