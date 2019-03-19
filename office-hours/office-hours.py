#!/usr/bin/python3
import sys
import re

lines = sys.stdin.readlines()
for count, line in enumerate(lines):
    m = re.match(r"(?P<identity>[^(]*) \((?P<role>.*)\)$", line)

    # really quick mock
    (average_response, last_response, last_patch) = ("74 hours", "three days ago", "five days ago")

    if not m.group('role').startswith("open list"):
        print("%s:" % m.group('identity'))
        print("  Average response time (in the last six months): %s" % average_response)
        print("  Last seen responding to patches: %s" % last_response)
        print("  Last seen sending patches: %s" % last_patch)

