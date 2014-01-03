#! /usr/bin/env python
# coding: utf-8


def is_palindrome(example):
    return example == example[::-1]

if __name__ == '__main__':
    example = 'syasdnkfnl'
    result = 'yangnay'
    print is_palindrome(example)
    print is_palindrome(result)
