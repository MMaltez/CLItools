#!/bin/sh
## Reduces number of colors in a image to 252 or less.

print_usage() {
cat << USAGE
Creates a reduced color version of the original image.
Usage:
  $0 <infile> <outfile> -c [colors]
Options:
  -h, --help        prints help message
  -c, --colors [nr] defaults to 252 colors
Positional arguments:
  <infile> input image file
  <outfile> output image file
Examples:
  1. Generate 15 or less color version of original image
  $ $0 original.png 15color.gif --colors 15
USAGE
}

print_help() {
	print_usage
	printf "\n"
	printf "Copyright (c) 2019 Miguel Maltez Jose\n"
}


########
# MAIN #
########

colors=252
nonoptcount=0
posargs=()

if [ "$#" -ge 2 ]
then
	infile="$1"
	outfile="$2"
else
	print_help
	exit 0
fi
while [ "$#" -gt 0 ]
do
	case "$1" in
		-h | --help )
			print_help
			exit 0
			;;
		-c | --colors )
			if [ -z "$2" ]
			then
				print_help
				exit 1
			else
				colors=$2
				shift
			fi
			;;
		-? | --* )
			printf "unknown option %s\n" "$1"
			;;
		* )
			nonoptcount=$((nonoptcount+1))
			posargs[$nonoptcount]="$1"
			;;
	esac
	shift
done

infile="${posargs[1]}"
outfile="${posargs[2]}"
[ -z "$outfile" ] && outfile="out.png"

if [ -f "$infile" ]
then
	magick convert "$infile" +dither -colors ${colors} "$outfile"
else
	echo "ERROR: $infile does not exist."
	exit 1
fi
exit 0
