#! /usr/bin/env python
# coding: utf-8


def fibo(num):
    for i in range(num):
        if i < 2:
            print i
            first = 0
            second = 1
        else:
            first, second = second, first + second
            print second


if __name__ == '__main__':
    fibo(100)
