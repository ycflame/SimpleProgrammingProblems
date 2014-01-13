#! /usr/bin/env python
# coding: utf-8


def on_all(func, t):
    return [func(i) for i in t]

if __name__ == '__main__':
    def perfect_squares(x):
        return x ** 2

    example = [i for i in range(1, 21)]
    print on_all(perfect_squares, example)
