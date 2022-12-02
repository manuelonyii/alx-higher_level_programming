#!/usr/bin/python3
if__name__== "__main__":
"""Printthe addition of all arguments."""
importsys

total= 0
fori in range(len(sys.argv) - 1):
total+= int(sys.argv[i + 1)]
print("{}".format(total))
