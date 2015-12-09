# -*- coding: utf-8 -*-

'''
ex29.py
What If
'''

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

'''
Key points:
1. Evaluate the conditions carefully.
2. The truth of the condition determines the flow of the program.
3. x += y is the short form of x = x + y. 
'''