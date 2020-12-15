#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_tuple = []
    a = len(tuple_a)
    b = len(tuple_b)
    for index in range(0, 2):
        if a == 0 and b == 0:
            sum_tuple.append(0)
        elif b > a and index > (a - 1):
            sum_tuple.append(tuple_b[index])
        elif a > b and index > (b - 1):
            sum_tuple.append(tuple_a[index])
        else:
            sum_tuple.append(tuple_a[index] + tuple_b[index])
    return tuple(sum_tuple)
