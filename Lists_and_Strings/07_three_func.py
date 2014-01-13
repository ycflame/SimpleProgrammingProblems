#! /usr/bin/env python
# coding: utf-8


def for_sum(t):
    result = 0
    for i in t:
        result += i
    return result


def while_sum(t):
    result = 0
    length = len(t)
    i = 0
    while i < length:
        result += t[i]
        i += 1

    return result


def recursion_sum(t):
    if len(t) == 0:
        raise

    if len(t) == 1:
        return t[0]

    return t[0] + recursion_sum(t[1:])

if __name__ == '__main__':
    example = [4, 5, 2, 7, 34, 67, 0, 1]
    print sum(example)
    print for_sum(example)
    print while_sum(example)
    print recursion_sum(example)
