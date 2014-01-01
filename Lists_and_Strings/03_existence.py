#! /usr/bin/env python
# coding: utf-8

def is_in(sample_li, element):
    return element in sample_li

if __name__ == '__main__':
    example = [2, 3, '65', 6.9]
    element = 'yang'
    print is_in(example, element)
