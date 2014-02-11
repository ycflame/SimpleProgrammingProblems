#! /usr/bin/env python
# coding: utf-8


def alternative(t1, t2):
    min_len = min(len(t1), len(t2))
    result = []
    for i in range(min_len):
        result.extend([t1[i], t2[i]])

    return result + t1[min_len:] + t2[min_len:]

if __name__ == '__main__':
    t1 = [1, 2, 3, 4, 5, 6]
    t2 = [7, 8, 9, 10, 11, 12, 13, 14]
    print alternative(t1, t2)
