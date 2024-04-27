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
from submissions.accepted import frieren_math

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'meteors! scary!'


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    """

    def __init__(self, B, L, E):
        self.B = B
        self.L = L
        self.E = E    


def make_sample_tests():
    """
    Make all sample test files.
    
    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    """
    main_sample_cases = [TestCase(20, 200, 10),
                         TestCase(80, 170, 40),
                         TestCase(100, 20, 5),
                         TestCase(40, 100, 10),
                         TestCase(15, 20, 30)
                         ] 
    make_sample_test(main_sample_cases, 'main')


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    """
    for i in range(10):
        cases = []
        for j in range(100):
            cases.append(TestCase(random.randint(1, 2000), random.randint(20, 2000), random.randint(0, 49)))
        make_secret_test(cases, 'main_random_0' + str(i))
    
    for i in range(10):
        cases = []
        for j in range(100):
            cases.append(TestCase(random.randint(1, 10 ** 8), random.randint(20, 10 ** 8), random.randint(0, 49)))
        make_secret_test(cases, 'bonus_random_0' + str(i))


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    T = len(cases)
    assert 0 <= T <= 100
    print(T, file=file)
    for case in cases:
        B, L, E = case.B, case.L, case.E
        assert 1 <= B <= 10 ** 8
        assert 20 <= L <= 10 ** 8
        assert 0 <= E <= 49
        print(f'{case.B} {case.L} {case.E}', file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    """
    for case in cases:
        print(frieren_math.solve(case.B, case.L, case.E), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
