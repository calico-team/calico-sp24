#!/bin/python
import sys

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


def check_case(is_reference, values, test_out, case):
    # Read first line of output
    first_line = read_file(test_out).split() if is_reference else read().split()

    # If the line is impossible then we don't read anything else
    if len(first_line) == 1 and first_line[0] == '-1':
        return False

    # Read the line
    for x in first_line:
        if not x.isdigit():
            print(f'Test #{case}: [Reference? {is_reference}] : An element on the first line is not a number',
                  f'{first_line}',
                  f'{x}')
            if is_reference:
                exit(1)
            else:
                return False

    if len(first_line) != 4:
        print(f'Test #{case}: [Reference? {is_reference}] : The line does not contain exactly 4 elements',
              f'{first_line}',
              f'{len(first_line)}')
        if is_reference:
            exit(1)
        else:
            return False

    solution = [int(x) for x in first_line]

    # Check that the second line is correct
    a, b, c, d = solution
    # Build the result
    result = values[0][a:a+b] + values[0][c:c+d]

    # Check that the result match the second string
    if values[1] != result:
        print(f'Test #{case}: [Reference? {is_reference}] : The resulting string do not match',
              f'{values}',
              f'{result}',
              f'{solution}',
              )
        if is_reference:
            exit(1)
        else:
            return False

    return True


def compare(test_in, test_out):
    T = int(read_file(test_in))
    for case in range(1, T + 1):

        # Read input from input file
        values = [read_file(test_in) for x in range(2)]
        reference_possible = check_case(True, values[:], test_out, case)
        contestant_possible = check_case(False, values[:], test_out, case)

        if reference_possible and not contestant_possible:
            print(f'Test #{case}: [Reference? False] : Contestant says its impossible but its possible')
        elif not reference_possible and contestant_possible:
            print(f'Test #{case}: [Reference? True] : Reference says its impossible but its possible',
                  'If this happens do not call Nacho he wont write a single python line anymore')
            exit(1)
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
