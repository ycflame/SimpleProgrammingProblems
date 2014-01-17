#! /usr/bin/env python
# coding: utf-8


def merge(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    i, j = 0, 0
    result = []
    while i < len1 and j < len2:
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    if i < len1:
        result += list1[i:]
    elif j < len2:
        result += list2[j:]

    return result

if __name__ == '__main__':
    print merge([2, 3, 4, 6], [5, 7, 9, 11, 23])
    print merge([], [5, 7, 9, 11, 23])
    print merge([], [])
