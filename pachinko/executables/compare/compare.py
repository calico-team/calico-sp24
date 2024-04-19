import sys
from collections import deque
from itertools import groupby

EPS = 1E-5

def main():
    if len(sys.argv) != 3:
        print('Incorrect number of arguments')
        exit(1)
    _, test_in_path, test_out_path = sys.argv

    try:
        with open(test_in_path, 'r') as test_in:
            with open(test_out_path, 'r') as test_out:
                compare(test_in, test_out)
    except IOError:
        print('Failed to open test input')
        exit(1)


def compare(test_in, test_out):
    T = int(read_file(test_in))
    for case in range(1, T + 1):

        # We assume that judge solution is correct. We just need to check for precision.
        judge_solution = float(read_file(test_out))

        # Read solution from the contestant
        contestant_solution = read().split()
        # Check that it is just one number
        if len(contestant_solution) != 1:
            print(f'Test #{case}: Contestant outputs more than one string per line')
        # Check that it is a floating point number
        keep_judging = False
        try:
            contestant_solution = float(contestant_solution[0])
            keep_judging = True
        except ValueError:
            print(f'Test #{case}: Contestant does not print a floating point number')

        if keep_judging and abs(contestant_solution - judge_solution) > EPS:
            print(f'Test #{case}: Contestant solution and judge solution '
                  f'differ by {contestant_solution - judge_solution} > {EPS}')

    try:
        temp = ''
        while not temp:
            temp = input().strip()
        print('Trailing output when judge expected no more output')
    except:
        pass


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
