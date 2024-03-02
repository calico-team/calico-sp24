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

import random, string
from calico_lib import make_sample_test, make_secret_test, make_data

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'TODO Change this to something different, long, and arbitrary.'


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
    """


    def __init__(self, A, B):
        self.A = A
        self.B = B


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
            TestCase("calico", "licoca"),
            TestCase("caliconcatenation", "calicocaliconcatenation"),
            TestCase("aaaaaa", "aaaaaaaaaaa"),
            TestCase("caliconcatenation", "tencalico"),
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

    def rand_str(n, c_cnt=26):
        return ''.join(random.choice(string.ascii_lowercase[:c_cnt]) for i in range(n))

    def get_random_substr(s, n):
        """
        Get a random substr of s with length n
        """
        l = len(s)
        assert n <= l
        pos = random.randint(0, l-n);
        return s[pos:pos+n]
    def make_random_bad(len1, len2):
        s1 = rand_str(len1)
        s2 = rand_str(len2)
        return TestCase(s1, s2)
    def make_random_good(len1, len2):
        s1 = rand_str(len1)
        splitPos = random.randint(len2-len1, min(len2-1, len1))
        s2 = get_random_substr(s1, splitPos)+get_random_substr(s1, len2-splitPos)
        return TestCase(s1, s2)

    def make_random_case(len1, len2):
        if random.randint(1, 2) == 1:
            return make_random_bad(len1, len2)
        return make_random_good(len1, len2)

    main_edge_cases = [
    ]
    # make_secret_test(main_edge_cases, 'main_edge')

    for i in range(5):
        main_random_cases = [make_random_case(10, 15) for _ in range(10)]
        make_secret_test(main_random_cases, 'main_random')


def make_test_in(cases: list[TestCase], file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    
    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        print(f'{case.A} {case.B}', file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """
    from submissions.accepted.n_cube import solve
    for case in cases:
        print(f"solving {len(case.A)} {len(case.B)}")
        print(solve(case.A, case.B), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
