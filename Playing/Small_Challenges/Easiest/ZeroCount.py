#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:31:00 2021

@author: diegobarbosa
"""
def end_zeros(num:int)->int:
    num=str(num)[::-1]
    count=0
    for i in num:
        if i=='0':
            count=count+1
        if i!='0':
            break
    return count


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Checked!")

