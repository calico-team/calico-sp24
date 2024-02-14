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
from alphabet_randomizer import AlphabetRandomizer

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = '217countsOfTaxEvasion?Rookienumbers'


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
    """


    def __init__(self, N, M, P, C):
        self.N = N
        self.M = M
        self.P = P
        self.C = C


def make_sample_tests():
    """
    Make all sample test files.
    
    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    
    TODO Write sample tests. Consider creating cases that help build
    understanding of the problem, help with debugging, or possibly help
    identify edge cases.
    """

    main_sample_cases = [
        TestCase(3, 4, [*"AAB"], [*"CABA"]),
        TestCase(5, 6, [*"SUSSY"], [*"MONGUS"]),
        TestCase(3, 3, [*"ABC"], [*"XYZ"]),
        TestCase(10, 1, [*"OOOOOOOOOO"], [*"N"]),
        TestCase(4, 11, [*"XYZY"], [*"AABCACBBACA"])
    ]
    make_sample_test(main_sample_cases, 'main')


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    
    TODO Write sample tests. Consider creating edge cases and large randomized
    tests.
    """

    main_secret_basic_cases = [
        TestCase(1, 1, [*"A"], [*"B"]),
        TestCase(1, 1, [*"A"], [*"A"]),
        TestCase(1, 2, [*"A"], [*"BA"]),
        TestCase(2, 1, [*"BA"], [*"A"]),
        TestCase(2, 1, [*"AB"], [*"A"]),
        TestCase(1, 2, [*"A"], [*"AB"]),
        TestCase(3, 3, [*"ABC"], [*"ABC"]),
        TestCase(3, 3, [*"XXX"], [*"XXX"]),
        TestCase(5, 6, [*"HJKLM"], [*"HJKLMN"]),
        TestCase(22, 21, [*"AAAAAAEAAAAAAAAAAAAAAA"], [*"AAAFAAAAAAAAAAAAAAAEA"])
    ]

    make_secret_test(main_secret_basic_cases, 'main_basic')

    main_secret_longer_cases = [
        TestCase(12, 6, [*"HUNGRYHUNGRY"], [*"HIPPOS"]),
        TestCase(10, 11, [*"AVOIDTAXES"], [*"SAIDTHEBEAR"]),
        TestCase(5, 3, [*"NOCAP"], [*"ONG"]),
        TestCase(6, 4, [*"GOOGOO"], [*"GAGA"]),
        TestCase(3, 2, [*"OBY"], [*"TO"]),
        TestCase(25, 25, [*"ABCDEFGHIJKLMNOPQRSTUVWXY"], [*"ZYXWVUTSRQPONMLKJIHGFEDCB"]),
        TestCase(25, 9, [*"WAWAWAWAWAWAWAWAWAWAWAWAW"], [*"IMTHEBABY"]),
        TestCase(6, 22, [*"CALICO"], [*"DOTCSDOTBERKELEYDOTEDU"]),
        TestCase(15, 15, [*"YOUUSEDTOCALLME"], [*"ONYOURCELLPHONE"]),
        TestCase(12, 11, [*"CALICOSPRING"], [*"TWENTYTHREE"]),
    ]

    make_secret_test(main_secret_longer_cases, 'main_longer')

    def generate(n, m, amount, alphabet, dist):
        cur_n, cur_m, cases = 0, 0, []
        while cur_n < n and cur_m < m and len(cases) < amount:
            add_n, add_m = min(n-cur_n, dist()), min(m-cur_m, dist())
            case = TestCase(add_n, add_m, [alphabet.pick() for _ in range(add_n)], [alphabet.pick() for _ in range(add_m)])
            cases.append(case)
            cur_n += add_n
            cur_m += add_m
        return cases

    def random_n_digit_number(n):
        return random.randint(10 ** (n - 1), (10 ** n) - 1) if n != 0 else 0
    
    def pick_dist(lim):
        if random.random() < 0.66: return lambda: random_n_digit_number(max(1, len(str(lim)))-1)
        else: return lambda: random.randrange(1, max(2, (lim+1)//2))

    for _ in range(5):
        bonus_random_cases = generate(10**5, 10**5, 100, AlphabetRandomizer("size"), pick_dist(10**5))
        make_secret_test(bonus_random_cases, 'bonus_random')
    

def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    
    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    total_N, total_M = 0, 0
    for case in cases:
        assert len(case.P) == case.N and len(case.C) == case.M, f"{case.N} {case.M}\n{case.P}\n{case.C}"
        total_N += case.N
        total_M += case.M
        print(f'{case.N} {case.M}', file=file)
        print(" ".join(case.P), file=file)
        print(" ".join(case.C), file=file)
        # print(total_N, total_M, total_N + total_M)
    assert total_N <= 10 ** 5 and total_M <= 10 ** 5


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """
    from submissions.accepted.quickstack_map import solve
    import sys
    real_stdout = sys.stdout
    sys.stdout = file
    for case in cases:
        assert len(case.P) == case.N and len(case.C) == case.M, f"{case.N} {case.M}\n{case.P}\n{case.C}"
        solve(case.N, case.M, case.P, case.C)
    sys.stdout = real_stdout


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
