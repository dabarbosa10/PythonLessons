#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:39:37 2021

@author: diegobarbosa
"""

def backward_string_by_word(text: str):
    a=[]
    ns=text.count(' ')
    sl=text.split(' ',ns)
    for i in range(len(sl)):
        a.append(sl[i][::-1])
    L=" ".join(a)
    return L


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Cool!")
