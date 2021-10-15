#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 12:06:18 2021

@author: diegobarbosa
"""
def first_word(cadena):
    text=""
    for letter in cadena:
        if letter.isspace()==True:
            break
        else:
            text=text+str(letter)
    return text


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    

