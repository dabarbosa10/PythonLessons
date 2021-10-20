#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 20:00:13 2021

@author: diegobarbosa
"""
import string 

def is_all_upper(text:str):
    uppercase=string.ascii_uppercase
    lowercase=string.ascii_lowercase
    for letter in text:
        if letter in lowercase:
            return False
    return True

if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('all lower'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('444') == True
    assert is_all_upper('55 55 5') == True
    print("Coding complete? Cool!")
        


