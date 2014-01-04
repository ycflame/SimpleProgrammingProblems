# coding:utf-8


def main():
    num = raw_input("Now, say a number: ")
    if num.isdigit():
        num = int(num)
        print num * (num + 1) / 2
    else:
        print 'I say a number, dear =.='

if __name__ == '__main__':
    main()
