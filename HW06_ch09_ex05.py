#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: [type here]
#   - # of words that use all aeiouy: [type here]
##############################################################################
# Imports

# Body

def uses_all(word, string_letter):
    result = None
    for letter in string_letter.lower():
        if letter not in word.lower():
            result = False
            break
        else:
            result = True
    return result

def use_aeiou_y():
    count_aeiou = 0
    count_aeiouy = 0
    with open('words.txt', 'r') as fin:
        for line in fin:
            word = line.strip()
            if uses_all(word, 'aeiou') == True:
                count_aeiou += 1
            if uses_all(word, 'aeiouy') == True:
                count_aeiouy += 1
    print("words that use all aeiou: {}".format(count_aeiou))
    print("words that use all aeiouy: {}".format(count_aeiouy))


##############################################################################
def main():
    print(uses_all('apple', 'ae'))
    print(uses_all('Edward', 'aeiou'))
    print(uses_all('phone', ''))

    use_aeiou_y()

if __name__ == '__main__':
    main()
