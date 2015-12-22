# Pysearch3  is a python search function.  Pysearch3 can either search for text or binary content, 
# depending on what command line arguments are provided.  Note that you will need to search for encrypted 
# or otherwise altered data in the altered form

import os
import argparse
import sys

def Main()
	# Checks for a valid version of python and quites if not found
	if(sys.version_info < 3):
		print("Python 3 required, please check github/Dozekar for pysearch to run in python 2")
		quit()
	
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
	
	# The main control loop for the program. It cycles around os.walk iteration
	if os.path.exists(args.target) and (os.path.exists(args.outputFile) or args.printFlag):
		walk_record = os.walk(args.target)
		for root, dirs, files in walk_record:
			parse_source(root, 'dir', args)
			for a_file in files
				parse_source(a_file, 'file', args)

		
		
	
	
if __name__= '__main__':
	Main()
