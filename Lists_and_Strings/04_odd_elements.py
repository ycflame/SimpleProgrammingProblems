#! /usr/bin/env python
# coding: utf-8


def odd_elements(example):
    return example[0::2]

if __name__ == '__main__':
    example = [1, 2, 3, 4, 5, 6, 7]
    print odd_elements(example)
