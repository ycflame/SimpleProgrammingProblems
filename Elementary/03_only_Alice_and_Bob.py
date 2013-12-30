# coding:utf-8


def main():
    name = raw_input("What's your name, dear? ")
    if name in ['Alice', 'Bob']:
        print 'Happy new year, %s!' % name
    else:
        print "Eh, I don't know you :-P"

if __name__ == '__main__':
    main()
