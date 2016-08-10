#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body
def has_no_e(word):
    '''word: str'''
    if 'e' not in word.lower():
        return True
    else:
        return False

def print_no_e():    
    with open('words.txt', 'r') as fin:
        count = 0
        total = 0
        for line in fin:
            word = line.strip()
            if has_no_e(word) == True:
                print(word)
                count += 1  
            total += 1
        percentage = count/total * 100
        print('The percentage = {:.2f}%'.format(percentage))

##############################################################################
def main():
    # print(has_no_e("Yifei"))
    # print(has_no_e("INFO202"))
    # print(has_no_e("Evening"))
    print_no_e()

if __name__ == '__main__':
    main()
