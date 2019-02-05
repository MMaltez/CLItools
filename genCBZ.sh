#!/bin/sh
## Make zipped comic books from directories.
## @author Miguel Maltez Jose
## @created 20161106

print_usage() {
cat << USAGE
Generation of zipped comix book zip files from image directories.

Usage:
  $0 <DIR>

Options:
  -h, --help  prints help message

Positional arguments:
  DIR target directory

Examples:

  1. Generate CBZ file from directory $ $0 AtomBoy
USAGE
}

print_help() {
	print_usage
	printf "\n"
	printf "Copyright (c) 2016 Miguel Maltez Jose\n"
}

makeCBZ() {
	name=${1%/}
	7z a -tzip "$name.cbz" "$name/" -r -x!\*.DS_Store
}

########
# MAIN #
########

while [ "$#" -gt 0 ]
do
	case "$1" in
		-h | --help )
			print_help
			exit 0
			;;
		-? | --* )
			printf "unknown option %s\n" "$1"
			;;
		* )
			if [ -d "$1" ]
			then
				makeCBZ "$1"
			fi
			;;
	esac
	shift
done
