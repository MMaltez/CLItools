#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Show initials that haven't been used in by the filenames in the current
directory.

This python script is replicating the functionality of a previous one written
in bash.

@author Miguel Maltez Jose
@created 20180529
@date    20190215
"""
import os

numbers = "0123456789"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
fullalphabet = numbers + alphabet_upper + "_" + alphabet_lower

def main():
	import argparse
	parser = argparse.ArgumentParser(description="Show unused initials.")
	parser.add_argument("-i", "--caseinsensitive"
		, help="sets the search of initials to be case insensitive"
		, action="store_true"
		, default=False
	)
	parser.add_argument("-u", "--used"
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
	if args.caseinsensitive:
		global fullalphabet
		fullalphabet = "_" + numbers + alphabet_upper
		used_initials = { letter.upper() for letter in used_initials }
	# print results
	if args.verbose:
		for letter in fullalphabet:
			if not letter in used_initials:
				print("\033[1m%s\033[0m" % letter, end="")
			else:
				print("\033[2m%s\033[0m" % letter, end="")
		print()
	elif args.used:
		print(
			"".join(
				sorted(
					list(used_initials)
				)
			)
		)
	else:
		print("\033[34m", end="")
		for letter in fullalphabet:
			if not letter in used_initials:
				print(letter, end="")
		print("\033[0m")

if __name__ == "__main__":
	main()
