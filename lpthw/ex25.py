# -*- coding: utf-8 -*-

'''
ex25.py
Even More Practice
'''

def break_words(stuff): 
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words): 
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): 
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words): 
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence): 
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence): 
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence): 
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

'''
Key points:
1. Learn how to use code in IDLE.
2. Two ways of import:
import ex25
from ex25 import ...
3. When you import a module, there should be a .pyc file.
'''