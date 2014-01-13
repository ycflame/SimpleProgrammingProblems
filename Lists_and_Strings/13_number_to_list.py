#! /usr/bin/env python
# coding: utf-8


def num2list(num):
    return [int(i) for i in str(num)]

if __name__ == '__main__':
    example = 39274
    print num2list(example)
