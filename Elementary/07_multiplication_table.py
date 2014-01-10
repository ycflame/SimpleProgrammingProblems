#! /usr/bin/env python
# coding: utf-8


def multi_table(number):
    for i in range(0, number + 1):
        if i == 0:
            i += 1
        else:
            print i,

        for j in range(1, number + 1):
            print '\t%s' % (i * j),
        print '\n'

if __name__ == '__main__':
    example = 12
    multi_table(12)
