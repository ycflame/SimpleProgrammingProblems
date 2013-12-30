#! /usr/bin/env python
# coding: utf-8


def rectangle(word_li):
    width = len(max(word_li, key=lambda x: len(x)))
    print '*' * (width + 4)
    for word in word_li:
        print '* ' + word + ' ' * (width - len(word)) + ' *'
    print '*' * (width + 4)

if __name__ == '__main__':
    word_li = ['Hello', 'World', 'in', 'a', 'rectangle']
    rectangle(word_li)
