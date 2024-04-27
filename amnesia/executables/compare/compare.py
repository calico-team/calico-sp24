import collections
import itertools
import sys

def main():
    if len(sys.argv) != 3:
        print('Incorrect number of arguments')
        exit(1)
    program, test_in_path, test_out_path = sys.argv
    
    try:
        with open(test_in_path, 'r') as test_in:
            with open(test_out_path, 'r') as test_out:
                compare(test_in, test_out)
    except IOError:
        print('Failed to open test input')
        exit(1)

def compare(test_in, test_out):
    try:
        while True:
            last_line = input().strip()
    except EOFError:
        pass
    
    if not read_file(test_out) == last_line:
        print('WA: Final answer is incorrect.')

def read_file(file):
    try:
        return file.readline().strip()
    except EOFError:
        print('End of test input while judge expected more input')
        exit(1)

def read():
    try:
        return input().strip()
    except EOFError:
        print('End of output while judge expected more output')
        exit()

if __name__ == '__main__':
    main()
