#!/usr/bin/python

from argparse import ArgumentParser

def GenerateStackMarker(n = 300):
    ret, char_0, char_a, char_A = "", ord('0'), ord('a'), ord('A')
    for i in range(n):
        s = chr(i // 1000 % 10 + char_A) \
          + chr(i // 100  % 10 + char_0) \
          + chr(i // 10   % 10 + char_a) \
          + chr(i         % 10 + char_0)
        ret += s
    return ret

parser = ArgumentParser()
parser.add_argument("-l", "--locate", dest="pattern", help="search for pattern in stack marker", metavar="FILE")
args = parser.parse_args()
mark = GenerateStackMarker()

if args.pattern:
    pos = mark.find(args.pattern)
    if pos >= 0:
        print "\n\nPattern %s found at index %i" % (args.pattern, pos)
    else:
        print "%s not found in the marker"
else:
    print "%s\n" % mark

