#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Convert leading spaces to tabs.

@author Miguel Maltez Jose
@created 20180525
"""
import sys

def spaceCount(line):
	"""Returns number of leading spaces."""
	i = 0
	while line[i] == " ":
		i += 1
	return i

def processFile(infile, outfile, identation=4):
	for line in infile:
		## space count
		sc = spaceCount(line)
		if sc % identation == 0:
			## tab count
			tc = sc // identation
			line = line.replace(" "*identation, "\t", tc)
		outfile.write(line)

def main():
	import argparse
	parser = argparse.ArgumentParser(description="Converts spaces to tabs.")
	parser.add_argument("infile"
		, help="input file, defaults to stdin."
		, type=argparse.FileType('r')
		, default=sys.stdin
	)
	parser.add_argument("outfile"
		, help="output file, defaults to stdout."
		, nargs='?'
		, type=argparse.FileType('w')
		, default=sys.stdout
	)
	parser.add_argument("-s", "--spaces"
		, help="number of spaces for each tab, defaults to 4"
		, default=4
	)
	args = parser.parse_args()

	processFile(args.infile, args.outfile, args.spaces)

if "__main__" == __name__:
    main()
