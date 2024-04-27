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

max_N = 100
max_T = 100

import os
import random
import numpy as np
from calico_lib import make_sample_test, make_secret_test, make_data

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'did you know we used to have a minecraft server? [citation needed]'


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    """

    def __init__(self, N, S, E):
        self.N = N
        self.S = S
        self.E = E

    def is_correct(self):
        if not (1 <= self.N <= max_N):
            return False
        if not (self.N == len(self.S) and self.N == len(self.E)):
            return False
        for i in range(self.N):
            if self.S[i] == '-' and self.E[i] == '#':
                return False
        return True


def make_sample_tests():
    """
    Make all sample test files.
    
    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    """
    main_sample_cases = [
        TestCase(6, "###--#", "-#----"),
        TestCase(7, "-####-#", "-####--"),
        TestCase(4, "----", "----"),
        TestCase(12, "#----##-#---", "#-----#-----"),
        TestCase(20, "###-#---###-#####--#", "#-#-----#---#--##---"),
    ]
    make_sample_test(main_sample_cases, 'main')


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    """

    np.random.seed(0)
    def random_cases(n, t):
        def one_case():
            start = ""
            end = ""
            while len(start) <= n:
                spacing = min(np.random.poisson(1), 4)
                start += "-" * spacing + "#"
                keep = random.randint(0, 1)
                if keep:
                    end += "-" * spacing + "#"
                else:
                    end += "-" * (spacing + 1)
            start = start[:n]
            end = end[:n]
            return TestCase(n, start, end)

        def ok_case():
            start = []
            for _ in range(n):
                start.append('-' if random.randint(0, 10) == 1 else '#')
            end = start[:]
            for k in range(n):
                cnt, j = 0, k
                while j < n and end[j] == '#' and cnt < 6:
                    j += 1
                    cnt += 1
                if cnt < 3:
                    continue
                take_away = random.randint(0, cnt - 2)
                for j in range(k + 1, k + 1 + take_away):
                    end[j] = '-'
            for k in range(n - 2):
                if end[k] == '#' and end[k+1] == '#' and end[k+2] == '#':
                    end[k+1] = '-'
            start = ''.join(start)
            end = ''.join(end)
            return TestCase(n, start, end)
        ans = []
        for _ in range(t):
            ans.append(one_case() if random.randint(0, 1) == 1 else ok_case())
        return ans

    for i in range(10):
        make_secret_test(random_cases(max_N, 100), 'main_random')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    file_name = os.path.basename(file.name)

    T = len(cases)
    assert 1 <= T <= max_T
    print(T, file=file)
    for case in cases:

        print(case.N, file=file)
        print(case.S, file=file)
        print(case.E, file=file)

        if 'main' in file_name:
            assert case.is_correct()
        else:
            raise 'bruh wtf u named ur test file wrong'

        # print(*case.sequences, file=file)

    if 'bonus_2' in file_name:
        assert (sum(case.N for case in cases) <= 10 ** 12)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    """
    from submissions.accepted.tntrun_ac import solve
    for case in cases:
        ans = solve(case.N, case.S, case.E)
        print(ans, file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
