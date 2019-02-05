#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Rename image files to sequential numbers ordered by modification time.

@author Miguel Maltez Jose
@date 20150427
"""
import os
import sys

def withargs():
	"""Rename image files in sequential numbers ordered by mtime."""
	pairs = []
	for filename in sys.argv[1:]:
		try:
			st = os.stat(filename)
			mtime = st.st_mtime
			pairs.append((mtime, filename))
		except OSError:
			print "Could not find file:", filename
	
	pairs.sort()
	counter = 0
	for mtime, oldfilename in pairs:
		counter += 1
		newfilename = str(counter).rjust(3,'0')
		newfilename += os.path.splitext(oldfilename)[1]
		os.rename(oldfilename, newfilename)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		withargs()
