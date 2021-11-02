#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 19:45:20 2021

@author: diegobarbosa
"""
def left_join(text: tuple) -> str:
    text=list(text)
    a=[]
    for i in range(len(text)):
        if 'right' not in text[i]:
            a.append(text[i])
        if 'right' in text[i]:
            b=text[i].replace('right', 'left')
            a.append(b)
    return ",".join(a)


if __name__ == "__main__":
    print("Example:")
    print(left_join(("left", "right", "left", "stop")))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
    ), "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Cool!")


