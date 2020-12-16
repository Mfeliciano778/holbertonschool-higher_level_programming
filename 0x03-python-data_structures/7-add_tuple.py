#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_tuple = []
    a = len(tuple_a)
    b = len(tuple_b)
    for index in range(0, 2):
        if a > index and b > index:
            sum_tuple.append(tuple_a[index] + tuple_b[index])
        elif b > a:
            sum_tuple.append(tuple_b[index])
        elif a > b:
            sum_tuple.append(tuple_a[index])
        else:
            sum_tuple.append(0)
    return tuple(sum_tuple)
