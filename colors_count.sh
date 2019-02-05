#!/bin/sh
## Counts number of unique colors of an image.
## @author Miguel Mlatez Jose
## @date 20180516

while [ $# -gt 0 ]
do
	magick identify -format "%k %wx%h %f\n" "$1"
	shift
done
exit 0
