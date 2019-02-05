#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Walks down a directory tree searching for potencial
case insentive file name conficts.

When copying a directory filled with files from my case sensitive file
systems, to an external HD drive formated in FAT, an error of file name
conflict whould sometimes arise after several minutes of copying. That error
left me with a directory partialy copied, which made me change a file name,
a try to copy it again, with no assurances that some other file whould
again trigger the same error, and leave a partial copy that had to be
repeated from the start.
Running this script on the directory prior to the copying signals all
filenames that have a case insentive name conflict.

@author Miguel Maltez Jose
@date 20150522
"""
import os
import argparse

def main():
	parser = argparse.ArgumentParser(description="""Find filenames that
	confict in case insentive file systems.""")
	parser.add_argument("dir", nargs='*', help="directory")
	args = parser.parse_args()
	
	for dirname in args.dir:
		# filter out non directory arguments
		if not os.path.isdir(dirname): continue
		for dirpath, dirnames, filenames in os.walk(dirname):
			freq = {}
			names = {}
			for name in dirnames + filenames:
				nameUpper = name.upper()
				freq[nameUpper] = freq.get(nameUpper, 0) + 1
				names[nameUpper] = names.get(nameUpper, []) + [name]
			for key, val in freq.iteritems():
				if val > 1:
					print "case confict found in:", dirpath
					for name in names[key]:
						print "\t%s" % name

if "__main__" == __name__:
	main()
