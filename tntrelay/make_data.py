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
SEED = 'is tnt a relay an iran vs palpatine anime battle reference? nwn'

max_N = 100
max_K = 100
max_T = 100


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
    """

    def __init__(self, N, K, S):
        self.N = N
        self.K = K
        self.S = S

    def is_correct(self):
        if not (1 <= self.N <= max_N):
            return False
        if not (1 <= self.K <= max_N):
            return False
        if self.N != len(self.S):
            return False
        # It must be possible to compete i.e. there must not be a substring of length K + 1 with all '-'
        cnt = 0
        for i in range(self.N):
            if self.S[i] not in ['-', '#']:
                return False
            if self.S[i] == '-':
                cnt += 1
                if cnt >= self.K + 1:
                    return False
            else:
                cnt = 0
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
        TestCase(6, 4, '###--#'),
        TestCase(7, 4, '-####-#'),
        TestCase(4, 4, '----'),
        TestCase(12, 5, '#----##-#---'),
        TestCase(20, 3, '###-#---###-#####--#')
    ]
    make_sample_test(main_sample_cases, 'main')

    # TODO add bonus if we make linear sol?


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    
    TODO Write sample tests. Consider creating edge cases and large randomized
    tests.
    """

    def make_random_string(_n, _k, prop1, prop2):
        """
        Creates random TNT run map of length N using jump K and prop1 / prop2 chance to place TNT instead of air
        """
        ans = []
        cnt = 0
        for _ in range(_n):
            if cnt == _k or random.randint(0, prop2 - 1) < prop1:
                ans.append('#')
                cnt = 0
            else:
                ans.append('-')
                cnt += 1
        return ''.join(ans)

    def create_infinity_case(_n):
        _n = min(_n, max_K)
        _k = random.randint(_n, max_K)
        s = make_random_string(_n, _k, 1, 2)
        return TestCase(_n, _k, s)

    def create_full_case(_n, _k):
        s = make_random_string(_n, _k, 1, 1)
        return TestCase(_n, _k, s)

    def create_random_case(_n, _k, prop1, prop2):
        s = make_random_string(_n, _k, prop1, prop2)
        return TestCase(_n, _k, s)

    for _ in range(10):
        batch = []
        for tc in range(max_T):
            rng = random.randint(1, 10)
            n = random.randint(9 * max_N // 10, max_N)
            k = random.randint(1, min(n - 1, max_K))
            if rng <= 8:
                # Just a random case
                batch.append(create_random_case(n, k, rng, 10))
            elif rng == 9:
                # Full case
                batch.append(create_full_case(n, k))
            else:
                # Infinity case
                batch.append(create_infinity_case(n))
        make_secret_test(batch, 'main_random')

    # TODO Think of edge cases maybe


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    
    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    assert 1 <= T <= max_T
    for case in cases:
        print(f'{case.N} {case.K}', file=file)
        print(case.S, file=file)
        assert case.is_correct()


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """
    from submissions.accepted.tntrelay_sliding_window import solve
    for case in cases:
        print(solve(case.N, case.K, case.S), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests,
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
