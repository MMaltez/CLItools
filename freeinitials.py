#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Show initials that haven't been used in by the filenames in the current
directory.

This python script is replicating the functionality of a previous one written
in bash.

@author Miguel Maltez Jose
@created 20180529
"""
import os

numbers = "0123456789"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
fullalphabet = "_" + numbers + alphabet_upper + alphabet_lower

def main():
	import argparse
	parser = argparse.ArgumentParser(description="Show unused initials.")
	parser.add_argument("--invert"
		, help="shows used initials instead of the ones not used"
		, action="store_true"
	)
	parser.add_argument("-v", "--verbose"
		, help="print out becomes more verbose"
		, action="store_true"
	)
	args = parser.parse_args()
	# process file names in current working directory
	cwdfiles = []
	for root, dirs, files in os.walk('.'):
		cwdfiles = files
		break
	used_initials = { os.path.basename(name)[0] for name in cwdfiles }
	# print results
	if args.verbose:
		for letter in fullalphabet:
			if not letter in used_initials:
				print("\033[1m%s\033[0m" % letter, end="")
			else:
				print("\033[2m%s\033[0m" % letter, end="")
		print()
	elif (args.invert):
		print(
			"".join(
				sorted(
					list(used_initials)
				)
			)
		)
	else:
		for letter in fullalphabet:
			if not letter in used_initials:
				print(letter, end="")
		print()

if "__main__" == __name__:
	main()
