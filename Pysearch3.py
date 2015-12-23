# Pysearch3  is a python search function.  Pysearch3 can either search for text or binary content, 
# depending on what command line arguments are provided.  Note that you will need to search for encrypted 
# or otherwise altered data in the altered form

import os
import argparse
import sys

def Main():
	# Checks for a valid version of python and quites if not found
	checkversion()
	
	# Sets up the argument parsing.  See documentation for argparse for more details
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', action='store', dest='target', default=os.getcwd(), help='Target file or directory.')
	parser.add_argument('-o', action='store', dest='outputFile' default=os.getcwd(), help='Output file.')
	parser.add_argument('-b', action='store_true', dest='binaryMode', default=False, help='Search for binary content.')
	parser.add_argument('-n', action='store_true', dest='namesOnly', default=False, help='Only search file and directory names.')
	parser.add_argument('-p', action='store_true', dest='printFlag', default=False, help='Prints to the console instead of to the file.')
	parser.add_argument('-r', action='store_true', dest='recordLine', default=False, help='record the whole line containing the data not just the line number and file.')
	
	# Initializes argments into args object
	args = parser.parse_args()
	
	
	if os.path.exists(args.target) and (os.path.exists(args.outputFile) or args.printFlag):
		if not args.printFlag:
			try:
				outputFileHandler = open(outputFile)
			except IOError as err:
				print('IO Error: {0}.  Quitting...'.format err)
				outputFileHandler.close()
				quit()
			
			# The main control loop for the program. It cycles around os.walk iteration
			walkRecord = os.walk(args.target)
			for root, dirs, files in walkRecord:
				parseSource(root, 'dir', args, outputFileHandler)
				for a_file in files:
					parseSource(a_file, 'file', args, outputFileHandler)
		outputFileHandler.close()
	print('Operation complete.')

# Verison check.  Notifies and quits if not verison 3 or if version 3 is below 3.3
def checkVersion():
	versionMain, versionMinor, verisonMicro, releaseLevel, serial = sys.version_info
	if not (versionMain == 3 and versionMinor > 3):
		print ('Python {0}.{1} is not a supported version', verisonMain, versionMinor)
		quit()
	
def parseSource(inputObject, inputObjectType, args, outputFileHandler):
		
		
	
if __name__= '__main__':
	Main()
