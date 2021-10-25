#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 13:53:53 2021

@author: diegobarbosa
"""


def split_pairs(a:str):
    n=len(a)
    split=[]
    if n==0:
        return split
    if (n%2!=0):
        a=a+'_'
        for i in range(0,n,2):
            split.append(a[i:i+2])
    elif(n%2==0):
        for i in range(0,n,2):
            split.append(a[i:i+2])
    return split
    

if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Cool!")