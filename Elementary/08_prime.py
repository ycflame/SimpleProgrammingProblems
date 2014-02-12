#! /usr/bin/env python
# coding: utf-8


def prime():
    num = 3
    candidate = [2, num]
    print 2
    while True:
        end = int(num ** 0.5) + 1
        for i in candidate:
            if i < end and num % i == 0:
                break
        else:
            print num
            candidate.append(num)

        num += 2

if __name__ == '__main__':
    prime()
