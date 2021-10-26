#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 20:47:01 2021

@author: diegobarbosa
"""

def linear_search(a_list,n):
    for i in a_list:
        if i==n:
            return True
    return False
    
if __name__ == '__main__':
    print("Example:")
    a=[1, 8, 32, 91, 5 , 15, 9, 100, 3]
    print(linear_search(a, 91))
    print(linear_search(a, 1003))