#!/usr/bin/env python
"""
Make test data for the problem.

To set up this script, do the following:
    - Set the seed to be something different, long, and arbitrary.
    - Set up the TestCase class to hold relevant information for your problem.
    - Write sample and secret tests in their respective functions.
    - Write input and output code in their respective functions.
Everything else will be handled by the make_data function in calico_lib.py.

You can also run this file with the -v argument to see debug prints.
"""

import random
from calico_lib import make_sample_test, make_secret_test, make_data

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 9034873104870

max_T = 10
max_N = 1000
max_M = 1000
max_total_N = 1000
max_total_M = 1000


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    """

    def __init__(self, N, M, G):
        self.N = N
        self.M = M
        self.G = G

    def is_correct(self):
        if not (1 <= self.N <= max_N):
            return False
        if not (1 <= self.M <= max_M):
            return False
        if len(self.G) != self.N:
            return False
        for i in range(self.N):
            if len(self.G[i]) != self.M:
                return False
        for i in range(self.N):
            for j in range(self.M):
                if self.G[i][j] not in "LDO":
                    return False
        if self.G[0][0] == 'L':
            self.G[0] = 'O' + self.G[0][1:]
        return True


def make_sample_tests():
    """
    Make all sample test files.
    
    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    """
    G1 = ["OD", "DO"]
    G2 = ["OLD", "ODO", "DLO"]
    G3 = [  # Minecraft case LOL
        "OLOLO",
        "LDOOD",
        "DOLLO",
        "OLODL",
        "ODLOD",
    ]
    G4 = [  # Impossible case
        "DLDL",  # haha grindr reference get it?
        "LDDL",
        "DOLL",
        "LOLO",
    ]

    main_sample_cases = [
        TestCase(2, 2, G1),
        TestCase(3, 3, G2),
        TestCase(5, 5, G3),
        TestCase(4, 4, G4),
    ]
    make_sample_test(main_sample_cases, 'main')


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    """

    weights = [
        # [O, L, D]
        [1, 1, 1],  # Equal probability
        [10, 1, 1],  # A lot of obsidian
        [1, 1, 10],  # Less obsidian and more diamonds
        [3, 1, 3],  # A bit of lava
        [3, 6, 9],  # TES 369 !!
        [3, 1, 0],  # No diamonds but check impossible case!!
        [0, 2, 5],  # Might find impossible solutions with a lot of diamonds.
    ]

    def weights_to_name(w):
        if w == weights[0]:
            return 'equal probability'
        elif w == weights[1]:
            return 'tons_of_obsidian'
        elif w == weights[2]:
            return 'tons_of_diamonds'
        elif w == weights[3]:
            return 'bit_of_lava'
        elif w == weights[4]:
            return '333666999'
        elif w == weights[5]:
            return 'only_coal'
        elif w == weights[6]:
            return 'diamonds_and_lava'

    def make_random_case(N, M, w):
        G = []
        for i in range(N):
            G.append('')
            for j in range(M):
                block = random.choices(['O', 'L', 'D'], weights=w)[0]
                G[i] += block
        return TestCase(N, M, G)

    # Make random small cases
    for w in weights:
        batch = []
        for _ in range(max_T):
            N = random.randint(9 * max_N // (max_T * 10), max_N // max_T)
            M = random.randint(9 * max_M // (max_T * 10), max_M // max_T)
            batch.append(make_random_case(N, M, w))
        random.shuffle(batch)
        make_secret_test(batch, f'main_random_small_{weights_to_name(w)}')

    # Make big cases
    for w in weights:
        for _ in range(2):
            batch = [make_random_case(max_N, max_M, w)]
            make_secret_test(batch, f'main_random_big_{weights_to_name(w)}')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    T = len(cases)
    assert 1 <= T <= max_T
    print(T, file=file)
    for case in cases:
        print(f'{case.N} {case.M}', file=file)
        for i in range(case.N):
            print(case.G[i], file=file)
        assert case.is_correct()


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """
    from submissions.accepted.lavapit_linear_memory_nacho import solve
    for case in cases:
        print(solve(case.N, case.M, case.G), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
