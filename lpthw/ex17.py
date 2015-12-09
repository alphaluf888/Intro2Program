# -*- coding: utf-8 -*-

'''
ex17.py
More Files
'''

from sys import argv
from os.path import exists

script, from_file, to_file  = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()
# This is how we make it in one line:
# indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
out_file = open(to_file, 'w')
out_file.write(indata)
print "Alright, all done."
out_file.close()
in_file.close()


'''
Key points:
1. Think about what is copying a file.
2. Finish the program using what you already know.
'''