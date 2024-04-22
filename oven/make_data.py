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
SEED = 'we making uncle gordon proud with this one 🗣🗣🗣🗣🗣🔥🔥🔥🔥🔥'


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    """

    def __init__(self, initial_D, As):
        self.initial_D = initial_D # Deja vu I've just been in this place before
        self.As = As


def make_sample_tests():
    """
    Make all sample test files.
    
    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    """
    main_sample_cases = [
        TestCase(41, 'DMII'),
    ]
    make_sample_test(main_sample_cases, 'main')


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    """
    make_secret_test([TestCase(1, 'I' * 500)], 'main_edge_increment')
    make_secret_test([TestCase(1000, 'D' * 500)], 'main_edge_decrement')
    make_secret_test([TestCase(500, 'M' * 500)], 'main_edge_maintain')
    
    def make_random_case():
        increment_bias = random.random()
        initial_D = random.randint(1, 1000)
        
        D = initial_D
        As = ''
        for _ in range(500):
            if random.randint(0, 1):
                As += 'M'
            elif D == 1 or D < 1000 and random.random() < increment_bias:
                As += 'I'
                D += 1
            else:
                As += 'D'
                D -= 1
        
        return TestCase(initial_D, As)
    
    for i in range(7):
        make_secret_test([make_random_case()], 'main_random')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    assert len(cases) == 1
    
    initial_D = cases[0].initial_D
    assert 1 <= initial_D <= 1000
    
    As = cases[0].As
    assert 1 <= len(As) <= 500
    assert set(As) | set('IDM') == set('IDM')
    
    print(initial_D, file=file)
    print(As, file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    """
    assert len(cases) == 1
    
    initial_D = cases[0].initial_D
    As = cases[0].As
    D = initial_D
    for A in As:
        if A == 'I':
            D += 1
        elif A == 'D':
            D -= 1
        assert 1 <= D <= 1000, f'D should be between 1 and 1000, was {D} instead'
        print(D, file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
