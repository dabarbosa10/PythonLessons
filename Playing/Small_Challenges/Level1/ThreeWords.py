#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 10:32:55 2021

@author: diegobarbosa
"""
def counter(text:str):
    text1=text.split(' ')
    j=0
    for i in range(len(text1)):
        if text1[i].isalpha():
            j+=1
        if text1[i].isalpha()==False: 
            j=0
        if j==3:
            return True
    return False      

if __name__ == '__main__':
    print('Example:')
    print(counter("Hello World hello"))
    
    assert counter("Hello World hello") == True, "Hello"
    assert counter("He is 123 man") == False, "123 man"
    assert counter("1 2 3 4") == False, "Digits"
    assert counter("bla bla bla bla") == True, "Bla Bla"
    assert counter("Hi") == False, "Hi"
    print("Coding complete? Cool!")

