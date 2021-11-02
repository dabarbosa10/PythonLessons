#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 07:29:28 2021

@author: diegobarbosa
"""

def second_index(text:str,symbol:str):
    if symbol not in text[::-1] or text.count(symbol)==1:
        return None
    else:
        a=text.index(symbol)
        b=text[a+1:].index(symbol)
    return a+b+1


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Cool')
