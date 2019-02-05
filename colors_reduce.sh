#!/bin/sh
## Reduces number of colors in a image to 252 or less.

print_usage() {
	printf "Usage:\n\t"
	printf "$0 <infile> <outfile>\n"
}

if [ $# -eq 2 ]
then
	magick convert "$1" +dither -colors 252 "$2"
else
	print_usage
fi

