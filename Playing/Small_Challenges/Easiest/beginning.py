#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:33:23 2021

@author: diegobarbosa
"""


def beginning_zeros(number: str) -> int:
    if int(number[0])!=0:
        count=0
    for i in range(len(number)):
        if int(number[i])!=0:
            break
        else: 
            count=i+1
    return count

if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Cool!")