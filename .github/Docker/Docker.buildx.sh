#! /bin/bash
# =============================================================================
# Authors:          Patrick Lehmann
#
# Entity:           STDOUT Post-Processor for Docker build
#
# License:
# =============================================================================
# Copyright 2017-2023 Patrick Lehmann - Boetzingen, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

# work around for Darwin (Mac OS)
READLINK=readlink; if [[ $(uname) == "Darwin" ]]; then READLINK=greadlink; fi

# Save working directory
WorkingDir=$(pwd)
ScriptDir="$($READLINK -f $(dirname $0))"
RootDir="$($READLINK -f $ScriptDir/..)"

ANSI_ENABLE_COLOR() {
	ENABLECOLOR='-c '
	ANSI_BLACK=$'\x1b[30m'
	ANSI_RED=$'\x1b[31m'
	ANSI_GREEN=$'\x1b[32m'
	ANSI_YELLOW=$'\x1b[33m'
	ANSI_BLUE=$'\x1b[34m'
	ANSI_MAGENTA=$'\x1b[35m'
	ANSI_CYAN=$'\x1b[36m'
	ANSI_DARK_GRAY=$'\x1b[90m'
	ANSI_LIGHT_GRAY=$'\x1b[37m'
	ANSI_LIGHT_RED=$'\x1b[91m'
	ANSI_LIGHT_GREEN=$'\x1b[92m'
	ANSI_LIGHT_YELLOW=$'\x1b[93m'
	ANSI_LIGHT_BLUE=$'\x1b[94m'
	ANSI_LIGHT_MAGENTA=$'\x1b[95m'
	ANSI_LIGHT_CYAN=$'\x1b[96m'
	ANSI_WHITE=$'\x1b[97m'
	ANSI_NOCOLOR=$'\x1b[0m'

	# red texts
	COLORED_ERROR="${ANSI_RED}[ERROR]"
	COLORED_FAILED="${ANSI_RED}[FAILED]${ANSI_NOCOLOR}"

	# yellow texts
	COLORED_WARNING="${ANSI_YELLOW}[WARNING]"

	# green texts
	COLORED_PASSED="${ANSI_GREEN}[PASSED]${ANSI_NOCOLOR}"
	COLORED_DONE="${ANSI_GREEN}[DONE]${ANSI_NOCOLOR}"
	COLORED_SUCCESSFUL="${ANSI_GREEN}[SUCCESSFUL]${ANSI_NOCOLOR}"
}
ANSI_ENABLE_COLOR

# command line argument processing
COMMAND=2  # 0-help, 1-unknown option, 2-no arg needed
INDENT=""
VERBOSE=0; DEBUG=0
while [[ $# > 0 ]]; do
	key="$1"
	case $key in
		-i|--indent)
			shift
			INDENT=$1
			;;
#		-v|--verbose)
#			VERBOSE=1
#			;;
#		-d|--debug)
#			VERBOSE=1
#			DEBUG=1
#			;;
		-h|--help)
			COMMAND=0
			;;
		*)		# unknown option
			echo 1>&2 -e "${COLORED_ERROR} Unknown command line option '$key'.${ANSI_NOCOLOR}"
			COMMAND=1
			;;
	esac
	shift # past argument or value
done

if [ $COMMAND -le 1 ]; then
	printf "%s\n" ""
	printf "%s\n" "Synopsis:"
	printf "%s\n" "  Script to filter Docker 'buildx' outputs."
	printf "%s\n" ""
	printf "%s\n" "Usage:"
	printf "%s\n" "  Docker.buildx.sh [-v][-d] [--help] [--indent <pattern>]"
	printf "%s\n" ""
	printf "%s\n" "Common commands:"
	printf "%s\n" "  -h --help             Print this help page."
	printf "%s\n" ""
	printf "%s\n" "Common options:"
#	printf "%s\n" "  -v --verbose          Print verbose messages."
#	printf "%s\n" "  -d --debug            Print debug messages."
	printf "%s\n" "  -i --indent <pattern> Indent all lines by this pattern."
	printf "%s\n" ""
	exit $COMMAND
fi

# Counters
Counter_Error=0

Pattern_CACHED='#[0-9]+ CACHED'
Pattern_FROM='#[0-9]+ \[([-a-zA-Z0-9]+ )?[0-9]+/[0-9]+\] FROM'
Pattern_RUN='#[0-9]+ \[([-a-zA-Z0-9]+ )?[0-9]+/[0-9]+\] RUN'
Pattern_COPY='#[0-9]+ \[([-a-zA-Z0-9]+ )?[0-9]+/[0-9]+\] COPY'
Pattern_LABEL_ENV='#[0-9]+ \[([-a-zA-Z0-9]+ )?[0-9]+/[0-9]+\] (LABEL|ENV)'
Pattern_DONE='#[0-9]+ DONE [0-9]+\.[0-9]+s'
Pattern_ERROR='(#[0-9]+ )?ERROR:'
Pattern_CANCELED='#[0-9]+ CANCELED'
Pattern_Tagging='#[0-9]+ naming to (.*?) done'
Pattern_MIKTEX='#[0-9]+ [0-9]+\.[0-9]+ Installing package'

while IFS='\n' read -r line; do
	if [[ "${line}" =~ $Pattern_FROM ]]; then
		printf "%s\n" "${INDENT}${ANSI_MAGENTA}${line}${ANSI_NOCOLOR}"
	elif [[ "${line}" =~ $Pattern_RUN ]]; then
		printf "%s\n" "${INDENT}${ANSI_CYAN}${line}${ANSI_NOCOLOR}"
	elif [[ "${line}" =~ $Pattern_COPY ]]; then
		printf "%s\n" "${INDENT}${ANSI_LIGHT_CYAN}${line}${ANSI_NOCOLOR}"
	elif [[ "${line}" =~ $Pattern_LABEL_ENV ]]; then
		printf "%s\n" "${INDENT}${ANSI_BLUE}${line}${ANSI_NOCOLOR}"
	elif [[ "${line}" =~ $Pattern_DONE ]]; then
		printf "%s\n" "${INDENT}${ANSI_GREEN}${line}${ANSI_NOCOLOR}"
	elif [[ "${line}" =~ $Pattern_ERROR ]]; then
		printf "%s\n" "${INDENT}${ANSI_LIGHT_RED}${line}${ANSI_NOCOLOR}"
	elif [[ "${line}" =~ $Pattern_CANCELED ]]; then
		printf "%s\n" "${INDENT}${ANSI_LIGHT_RED}${line}${ANSI_NOCOLOR}"
	elif [[ "${line}" =~ $Pattern_CACHED ]]; then
		printf "%s\n" "${INDENT}${ANSI_YELLOW}${line}${ANSI_NOCOLOR}"
	elif [[ "${line}" =~ $Pattern_Tagging ]]; then
		ImageName=${BASH_REMATCH[1]}
		printf "%s\n" "${INDENT}${ANSI_LIGHT_GREEN}${line}${ANSI_NOCOLOR}"
	elif [[ "${line}" =~ $Pattern_MIKTEX ]]; then
		printf "%s\n" "${INDENT}${ANSI_LIGHT_BLUE}${line}${ANSI_NOCOLOR}"
	else
		printf "%s\n" "${INDENT}${ANSI_LIGHT_GRAY}${line}${ANSI_NOCOLOR}"
	fi
done < "/dev/stdin"

if [[ -n "${ImageName}" ]]; then
	printf "%s\n" ""
	printf "%s\n" "Image size of '${ImageName}' is $(docker image inspect ${ImageName} --format='{{.Size}}' | numfmt --to=iec)"
fi

exit $Counter_Error
