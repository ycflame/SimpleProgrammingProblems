# coding:utf-8

import math


def main():
    num = raw_input("Now, say a number: ")
    if num.isdigit():
        num = int(num)
        result = 0
        choice = raw_input("choose 1 for sum or 2 for factorial:")
        if choice == '1':
            result += num * (num + 1) / 2
        elif choice == '2':
            result = math.factorial(num)
        else:
            print 'I say a number, dear =.='
            return

        print result

    else:
        print 'I say a number, dear =.='

if __name__ == '__main__':
    main()
