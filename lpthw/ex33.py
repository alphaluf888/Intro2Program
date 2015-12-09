# -*- coding: utf-8 -*-

'''
ex33.py
While Loops
'''

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    i = i + 1
    print "Numbers now: ", numbers 
    print "At the bottom i is %d" % i
    print "The numbers: "

for num in numbers:
    print num

'''
Key points:
1. while-loop is trickier than for-loop and only use it when you have to.
2. To avoid tricky things, there are some rules to follow:
  1) Review your while statements and make sure that the thing 
     you are testing will become False at some point.
  2) When in doubt, print out your test variable at the top AND bottom 
     of the while-loop to see what it's doing.
'''