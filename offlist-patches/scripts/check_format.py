#!/usr/bin/python3
#
# assume filename is provided as argument
#
# All files could be checked with:
# find . -name '[0-9a-f]*' | xargs -n 1 ../scripts/check_format.py
#

import sys
import re

# TODO: consider using argparse when it gets more complex
print("checking %s" % sys.argv[1])

filename = sys.argv[1]
current_section = ''
next_section = ''

with open(filename) as file:
    for cnt, line in enumerate(file):
        if cnt == 0:
            if re.match(r"^[0-9a-f]{40} .*$", line):
                #print("first line looks good")
                pass
            else:
                print('first line shall be "<git sha> <commit message header>": %s' % line)
        if cnt == 1:
            if re.match(r"^ASSESSMENT: (OFF-LIST PATCH|NOT MATCHED|NOT IN DATASET|REVERT|RELEASE COMMIT|UNCLEAR)", line):
                #print("second line looks good")
                pass
            else:
                print("Invalid value for ASSESSMENT: %s" % line)
        if re.match(r"^MESSAGE-ID:", line):
            if re.match(r"^MESSAGE-ID: [<].*[>]$", line):
                # print("looks okay: %s" % line)
                pass
            else:
                print("looks different: %s" %line)

        if line == "TODO:":
            # print("now in TODO section")
            next_section = "TODO"
        if re.match(r"^DETAILS:
        if current_section == "TODO":
            if (re.match(r"^    .*$", line)):
                # print("looks good")
                pass
            else:
                if (re.match(r"^  - (MAIL TO AUTHOR & MAINTAINER|PASTA|GIT HISTORY|DATASET):", line)):
                    # print("TODO section looks good")
                    pass
                else:
                    print("TODO section broke: %s" % line)
        current_section = next_section
#<git sha> <commit message header>
#ASSESSMENT: (OFF-LIST PATCH | NOT MATCHED | NOT IN DATASET | REVERT | INLINE PATCH | RELEASE COMMIT | UNCLEAR)
#MESSAGE-ID: [optional, reasonable when NOT MATCHED or NOT IN DATASET]
#DETAILS:
#CONFIDENCE: [optional]
#TODO:
#  - (MAIL TO AUTHOR & MAINTAINER | PASTA | GIT HISTORY | DATASET):

