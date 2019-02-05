#!/bin/sh
## Tells you what initials haven't been used yet.
## Useful for choosing names that are quick to autocomplete.
## @author Miguel Maltez Jose
## @created 20100530
## @date 20151208
## @date 20161002

fullalphabet="_ 0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z"

development_history() {
cat << DEVHISTORY
20161002 : a revision the algorithm for finding unused initials.
        ls is called once, instead of over 62 times!
DEVHISTORY
}

print_usage() {
cat << USAGE
Free Initials
  Shows letters still not used in initials of file or directory names.

Usage:
  $0 [-h] [-x] [DIR]

Options:
  -h, --help  prints help message
  -x          show used initials instead of free initials

Positional arguments:
  DIR target directory, defaults to current

Examples:

  1. unused initials in current directory
	$ $0
  2. used initials in images directory
	$ $0 -x images
USAGE
}

print_help() {
	print_usage
	printf "\n"
	printf "Copyright (c) 2010-2016 Miguel Maltez Jose\n"
}

seekLetters() {
	for letter in 0 1 2 3 4 5 6 7 8 9 _ \
	A B C D E F G H I J K L M N O P Q R S T U V W X Y Z _ \
	a b c d e f g h i j k l m n o p q r s t u v w x y z
	do
		if ls $letter* > /dev/null 2>&1
		then
			true
			#printf "\033[37m%c\033[0m" $letter
		else
			printf "\033[34m%c\033[0m" $letter
		fi
	done
	printf "\n"
}

listInitials() {
	# list full alphabet once
	for letter in $fullalphabet
	do
		printf "%s\n" $letter
	done
	# list initials used
	ls | while read file
	do
		# print first letter of file name
		printf "%s\n" "${file:0:1}"
	done
}

list_free_initials() {
	listInitials | sort | uniq -u |
	while read letter
	do
		printf "\033[34m%c\033[0m" $letter
	done
	printf "\n"
}

list_used_initials() {
	listInitials | sort | uniq -d |
	while read letter
	do
		printf "\033[33m%c\033[0m" $letter
	done
	printf "\n"
}

##########
## MAIN ##
##########

mode="free"
directory=""

while [ "$#" -gt 0 ]
do
	case "$1" in
		-h | --help )
			print_help
			exit 0
			;;
		--devhist )
			development_history
			exit 0
			;;
		-x )
			mode="used"
			;;
		-?* )
			printf "Unknown option: %s\n" "$1" >&2
			;;
		?* )
			[ -d "$1" ] && directory="$1"
			;;
		* )
			break
			;;
	esac
	shift
done

if [ -n "$directory" ]
then
	cd "$directory" || exit $?
fi

case $mode in
	free)
		list_free_initials
		;;
	used)
		list_used_initials
		;;
esac

exit 0
