#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:58:27 2021

@author: diegobarbosa
Ceasar Cipher. Taken from: The self-Taught Computer Scientist)
"""

import string 

def cipher(a_string, key):
    uppercase=string.ascii_uppercase
    lowercase=string.ascii_lowercase
    encrypt=''
    for c in a_string:
        if c in uppercase:
            new=(uppercase.index(c)+key)%26
            encrypt+=uppercase[new]
        elif c in lowercase:
            new=(lowercase.index(c)+key)%26
            encrypt+=lowercase[new]
        else:
            encrypt+=c
    return encrypt

if __name__ == '__main__':
    print("Word to cypher: Diego. Key: 2 ")
    print(cipher('Diego',2))


