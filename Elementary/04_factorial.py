# coding:utf-8

import math


def main():
    num = raw_input("Now, say a number: ")
    if num.isdigit():
        print math.factorial(int(num))
    else:
        print 'I say a number, dear =.='

if __name__ == '__main__':
    main()
