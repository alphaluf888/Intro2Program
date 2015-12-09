# -*- coding: utf-8 -*-

'''
ex15.py
Reading Files
'''

from sys import argv

script, filename = argv
txt = open(filename)
print "Here's your file %r:" % filename 
print txt.read()
# txt.close()

print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()
# txt_again.close()

'''
Key points:
1. Avoid any form of hard coding.
2. Remember to close files when you are done, 
   even Python do this for you at the end of the program.
3. This program cannot print the Chinese characters correctly.
'''