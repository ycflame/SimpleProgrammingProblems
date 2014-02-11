#! /usr/bin/env python
# coding: utf-8

import random


class Guess(object):

    def __init__(self, lower_bound=1, upper_bound=100, max_try=3):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.max_try = max_try
        self.secret = random.randint(1, 100)
        self.last_try = None
        self.guess()

    def guess(self):
        while self.max_try:
            guess_num = raw_input('Guess a number between %d and %d: ' % (self.lower_bound, self.upper_bound))
            if not guess_num.isdigit():
                guess_num = raw_input('Please input a number: ')
                continue

            guess_num = int(guess_num)
            if self.last_try is not None and self.last_try == guess_num:
                print "Don't stick to your wrong answer!"
                continue

            if guess_num < self.secret:
                print 'smaller than the answer'
            elif guess_num > self.secret:
                print 'bigger than the answer'
            else:
                print 'Congratulations!'
                return

            self.last_try = guess_num
            self.max_try -= 1

        print 'Sorry, the corrent answer is ', self.secret


if __name__ == '__main__':
    Guess()
