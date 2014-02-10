#! /usr/bin/env python
# coding: utf-8

from calendar import isleap
from datetime import datetime


def leap_year(N=20):
    current = datetime.now().year
    while not isleap(current):
        current += 1
    for i in range(N):
        print current
        current += 4

if __name__ == '__main__':
    leap_year()
