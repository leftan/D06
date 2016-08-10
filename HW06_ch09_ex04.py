#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1: he call coach
#       2: chef flee cafe
#       3: aloe cool face
##############################################################################
# Imports
 
# Body

def uses_only(word, string_letter):
    result = None
    for letter in word.lower():
        if letter not in string_letter.lower():
            result = False
            break
        else:
            result = True
    return result

def acefhlo_only():
    acefhlo_list = []
    with open("words.txt", "r") as fin:
        for line in fin:
            word = line.strip()
            if uses_only(word, 'acefhlo') == True:
                acefhlo_list.append(word)
    return acefhlo_list

##############################################################################
def main():
    print(uses_only('Apple', 'aelP'))
    print(uses_only('apply', 'aelp'))
    print(uses_only('appb', 'a'))

    print(acefhlo_only())
if __name__ == '__main__':
    main()
