#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 21:28:48 2021

@author: diegobarbosa
"""


def checkio(arrays: list) -> int:
    con=0
    if len(arrays)==0:
        return 0
    else:
        for i in range(0,len(arrays),2):
            con+=arrays[i]
    return con*arrays[-1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))
    
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Cool!")