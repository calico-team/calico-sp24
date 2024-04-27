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
SEED = 'TODO Change this to something different, long, and arbitrary.'

MAX_H = 2000
MAX_N = 1_000_000_000_000
MAX_M = 200_000
MAX_R = 2000
MAX_T = 1


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
    """

    def __init__(self, H, N, M, R):
        self.H = H
        self.N = N
        self.M = M
        self.R = R

    def __bool__(self):
        if not (1 <= self.H <= MAX_H):
            return False
        if not (1 <= self.N <= MAX_N):
            return False
        if not (1 <= self.M <= MAX_M):
            return False
        if len(self.R) != self.M:
            return False
        if not all([0 <= r <= MAX_R for r in self.R]):
            return False
        return True


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
        [TestCase(20, 2, 3, [10, 11, 11])],
        [TestCase(20, 2, 5, [9, 8, 7, 4, 0])],
        [TestCase(20, 2, 2, [10, 0])],
        [TestCase(1729, 1000, 10, [0, 0, 0, 1, 1, 1, 2, 2, 3, 4])],
    ]
    for tc in main_sample_cases:
        make_sample_test(tc, 'main')


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    
    TODO Write sample tests. Consider creating edge cases and large randomized
    tests.
    """

    def make_random_case(H, N, M):
        R = [random.randint(0, MAX_R) for _ in range(M)]
        zeros = random.randint(0, M // 10)
        for i in range(zeros):
            R[i] = 0
        R[-1] = random.randint(H, MAX_R)
        random.shuffle(R)
        return TestCase(H, N, M, R)

    for i in range(25):
        main_random_cases = [make_random_case(
            random.randint(9 * MAX_H // 10, MAX_H),
            random.randint(9 * MAX_N // 10, MAX_N),
            random.randint(9 * MAX_M // 10, MAX_M),
        )]
        make_secret_test(main_random_cases, 'main_random')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    
    TODO Implement this for your problem.
    """
    T = len(cases)
    assert 1 <= T <= MAX_T
    for case in cases:
        print(f'{case.H} {case.N} {case.M}', file=file)
        print(*case.R, file=file)
        assert case


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """
    print("Making new test")
    from submissions.accepted.maushold_fft import solve
    for case in cases:
        print(solve(case.H, case.N, case.M, case.R), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
