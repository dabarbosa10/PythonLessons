# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-2)+fib(n-1)
    
for i in range(1,20):
    print(fib(i))
    


