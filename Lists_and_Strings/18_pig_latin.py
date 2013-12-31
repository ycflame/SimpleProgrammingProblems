#! /usr/bin/env python
# coding: utf-8


def pig_latin(word_li):
    result = []
    for i, word in enumerate(word_li.split()):
        if i == 0:
            temp = (word[1:] + word[:1] + 'ay').capitalize()
        else:
            temp = (word[1:] + word[:1] + 'ay').lower()

        result.append(temp)

    return ' '.join(result)

if __name__ == '__main__':
    example = "The quick brown fox"
    print pig_latin(example)
