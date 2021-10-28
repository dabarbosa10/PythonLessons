#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:47:21 2021

@author: diegobarbosa
"""
def sum_numbers(text:str)->int:
    text=text.split()
    count=0
    for i in range(len(text)):
        if text[i].isdigit():
            count+=int(text[i])
    return count


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Cool")


