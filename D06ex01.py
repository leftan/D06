import os

def print_dir():
    os.chdir('/Users/leftan/pythonbootcamp/D05')
    print(os.listdir('/Users/leftan/pythonbootcamp/D05'))

def main():
    print_dir()

if __name__ == '__main__':
    main()        