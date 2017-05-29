#!/usr/bin/python3

import os
import time

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
	while 1:
		time.sleep (10)
		after = directory_listing(path_to_watch)
	
		added = [f for f in after if (not f in before and ".wav" in f)]
	
		if added:
			print("Added: ")
			print(added)

		before = after

if __name__ == '__main__':
	main()
