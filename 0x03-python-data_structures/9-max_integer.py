#!/usr/bin/python3

def max_integer(my_list=[]):
    m = None
    if len(my_list) > 0:
        maxi = my_list[0]
        for item in my_list:
            if item > m:
                m = item
    return m
