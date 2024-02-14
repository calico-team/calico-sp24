import sys
from itertools import groupby

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

cnt_fixed = lambda perm: sum(j + 1 == p for j, p in enumerate(perm))

def compare(test_in, test_out):
    T = int(read_file(test_in))
    for case in range(1, T + 1):
        N, M = tuple([int(x) for x in read_file(test_in).split(' ')])
        P = [x for x in read_file(test_in).split()]
        C = [x for x in read_file(test_in).split()]
        
        ref_str = ''.join(read_file(test_out).split(' '))
        submitted_str = ''.join(read().split(' '))

        for x in ref_str:
            if not (len(x) == 1 and x.isalpha() and x.isupper()):
                print(f'Test #{case}: reference contains invalid elements (all elements must be single uppercase letters).'
                    'The reference output is wrong.',
                    f'Item: {x}')
                exit(1)
        for x in submitted_str:
            if not (len(x) == 1 and x.isalpha() and x.isupper()):
                print(f'Test #{case}: submitted list contains invalid elements (all elements must be single uppercase letters).')
                continue
        
        if len(ref_str) != N + M:
            print(f'Test #{case}: reference list is the wrong length.'
                'The reference output is wrong.')
            exit(1)
        if len(submitted_str) != N + M:
            print(f'Test #{case}: submitted list is the wrong length.')
            continue
        
        if set(ref_str) != set(P).union(set(C)):
            print(f'Test #{case}: reference list contains elements not found in input and/or is missing elements from input.'
                'The reference output is wrong.')
            exit(1)
        if set(submitted_str) != set(P).union(set(C)):
            print(f'Test #{case}: submitted list contains elements not found in input and/or is missing elements from input.')
            continue

        submitted_chunks = [''.join(group) for _, group in groupby(submitted_str)]
        ref_chunks = [''.join(group) for _, group in groupby(ref_str)]

        if len(ref_chunks) != len(set(ref_str)):
            print(f'Test #{case}: reference didn\'t group similar elements together.'
                'The reference output is wrong.')
            exit(1)
        if len(submitted_chunks) != len(set(submitted_chunks)):
            print(f'Test #{case}: submitted list didn\'t group similar elements together.')
            continue
    
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