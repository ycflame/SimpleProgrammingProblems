#! /usr/bin/env python
# coding: utf-8


def pi(N=100000):
    result = 0
    for i in range(N):
        result += (-1) ** i * 1.0 / (2 * i + 1)

    return 4 * result

if __name__ == '__main__':
    print pi()
