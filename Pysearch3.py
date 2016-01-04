# Pysearch3  is a python search function.  Pysearch3 can either search for text or binary content, 
# depending on what command line arguments are provided.  Note that you will need to search for encrypted 
# or otherwise altered data in the altered form

import os
import argparse
import sys

#Main program loop and setup
def Main():
	# Checks for a valid version of python and quits if not found
	args = init()
	
	#verifies path is a valid path and getcwd()'s if it is not
	print('Checking if a target was specified in arguments')
	if not arg.target:
		print ('Target not specified in arguments. Getting CWD as Target.')
		targetPath = os.getcwd()
		print('{0} loading as target path.'.format targetPath)
	else:
		print('Target specified in arguments.')
		targetPath = args.target
	print('Checking if printing to file or console...')
	if not printFlag:
		print('Printing to file. \nChecking if an output file has been specified...')
		
	
	print('Verifying that the loaded paths exists...')
	if os.path.exists(targetPath) and (os.path.exists(outPath) or args.printFlag):
		print('Paths valid.')
		if not args.printFlag:
			try:
				outputFileHandler = open(outPath)
			except IOError as err:
				print('IO Error: {0}.  Quitting...'.format(err))
				outputFileHandler.close()
				quit()
			
			# The main control loop for the program. It cycles around os.walk iteration
			walkLoop(args, targetPath, outputFileHandler)
			outputFileHandler.close()
			print('Closing output file{0}...')
		else:
			print('Paths invalid: Closing program.\nPaths:\ntargetPath: {0}\noutPath: {1}'.format(targetPath, outPath))
			quit()
	print('Operation complete.')

# Verison check.  Notifies and quits if not verison 3 or if version 3 is below 3.3
def init
	versionMain, versionMinor, verisonMicro, releaseLevel, serial = sys.version_info
	if not (versionMain == 3 and versionMinor > 3):
		print ('Python {0}.{1} is not a supported version'.format(verisonMain, versionMinor))
		quit()
	else:
	
		# Sets up the argument parsing.  See documentation for argparse library for more details
		parser = argparse.ArgumentParser()
		parser.add_argument('-t', action='store', dest='target', default=False, help='Target file or directory.')
		parser.add_argument('-o', action='store', dest='outputFile' default=False, help='Output file.')
		parser.add_argument('-b', action='store_true', dest='binaryMode', default=False, help='Search for binary content.')
		parser.add_argument('-n', action='store_true', dest='namesOnly', default=False, help='Only search file and directory names.')
		parser.add_argument('-p', action='store_true', dest='printFlag', default=False, help='Prints to the console instead of to the file.')
		parser.add_argument('-r', action='store_true', dest='recordLine', default=False, help='record the whole line containing the data not just the line number and file.')
	
		# Initializes argments into args object
		return parser.parse_args()
		
#does the main walk loop through the directories	
def walkLoop(args, targetPath, outputFileHandler):
	# The main control loop for the program. It cycles around os.walk iteration
	walkRecord = os.walk(targetPath)
	for root, dirs, files in walkRecord:
		parseSource(root, 'dir', args, outputFileHandler)
		for a_file in files:
			parseSource(a_file, 'file', args, outputFileHandler)
	

def parseSource(inputObject, inputObjectType, args, outputFileHandler):
		
		
	
if __name__= '__main__':
	Main()
