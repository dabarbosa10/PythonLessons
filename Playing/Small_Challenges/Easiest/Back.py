#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:29:30 2021

@author: diegobarbosa
"""


def backward_string(val:str):
    val=val[::-1]
    return val

if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Great!")