# -*- coding: utf-8 -*-

'''
ex40.py
Modules, Classes and Objects
'''

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy_bday = Song(["Happy birthday to you",
                "I don't want to get sued",
                "So I'll stop right there"])
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

'''
Key points:
1. Modules are like dictionaries.
2. Classes are like modules.
3. Objects are like mini imports.
4. Understand 1-3 before you move on.
'''
