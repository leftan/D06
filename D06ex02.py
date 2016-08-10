import random

def random_num():
    with open('d06_ex2.txt', 'w') as fin:
        for i in range(10):
            fin.write(str(random.randint(0, 100)) + '\n')

def main():
    random_num()

if __name__ == '__main__':
    main() 