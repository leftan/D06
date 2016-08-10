#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body


def avoids(word, forbidden_letter):
    """ return True if word NOT forbidden"""
    for letter in word:
        if letter.lower() in forbidden_letter.lower():
            return False
            break
        else:
            return True


def forbidden_prompt():
    """ print count of words NOT forbidden by input"""
    user_input = str(input("Enter forbidden letters: "))
    count = 0
    with open('words.txt', 'r') as fin:
        for line in fin:
            if avoids(line, user_input) == True:
                count += 1
    print(count)


def forbidden_param(forbidden_letter):
    """ return count of words NOT forbidden by param"""
    count = 0
    with open('words.txt', 'r') as fin:
        for line in fin:
            if avoids(line, forbidden_letter) == True:
                count += 1
    return count

# def list_five():
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     letter_combination = []
#     five_letter = ''

#     while letter_combination
#         count_letter = 0
#         while count_letter < 5: 
#             for letter in alphabet:
#                 if letter not in five_letter:
#                     five_letter += letter
#                     count_letter += 1
#         letter_combination.append(five_letter)

#     if  


def list_recursive(alphabet):
    if alphabet 

def find_five():
    smallest = ''
    if forbidden_param('') > 



##############################################################################
def main():
    ...
    # Your final submission should only call five_five
    five_five()

if __name__ == '__main__':
    main()
