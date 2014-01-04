# coding:utf-8


def main():
    num = raw_input("Now, say a number: ")
    if num.isdigit():
        num = int(num)
        result = 0
        for i in range(num + 1):
            if i % 3 == 0 or i % 5 == 0:
                result += i

        print result
    else:
        print 'I say a number, dear =.='

if __name__ == '__main__':
    main()
