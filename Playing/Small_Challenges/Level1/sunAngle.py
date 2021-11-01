#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:07:21 2021

@author: diegobarbosa
"""
def sun_angle(time:str):
    time=time.split(':')
    GR=180/(12*60*60)
    if 6<=int(time[0])<=17:
        h=int(time[0])-6
        A=(h*60*60)+(int(time[1]))*60
        return GR*A
    if int(time[0])==18 and time[1]=='00':
        return 180
    else:
        return "I don't see the sun!"
    

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
