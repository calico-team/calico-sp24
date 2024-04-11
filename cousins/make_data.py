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
from bisect import bisect_right

from calico_lib import make_sample_test, make_secret_test, make_data

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'Cuanto mas primo mas me arrimo'


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    TODO Change this to store the relevant information for your problem.
    """

    max_N = 20_000
    max_M = 20_000
    max_A = 10_000_000

    def __init__(self, N, M, A, G):
        """
        :param N: size of the board
        :param M: number of games
        :param A: board description
        :param G: games description
        """
        self.N = N
        self.M = M
        self.A = A
        self.G = G

    def correct(self):
        if len(self.A) != self.N:
            return False
        if len(self.G) != self.M:
            return False
        if not (1 <= self.N <= TestCase.max_N):
            return False
        if not (1 <= self.M <= TestCase.max_M):
            return False
        for Ai in self.A:
            if not (1 <= Ai <= TestCase.max_A):
                return False
        for Gj in self.G:
            if len(Gj) != 2:
                return False
            if not (1 <= Gj[0] <= Gj[1] <= self.N):
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
        TestCase(
            N=10,
            M=6,
            A=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            G=[[6, 6], [5, 5], [1, 10], [3, 6], [7, 9], [5, 8]]
        ),
    ]
    for tc in main_sample_cases:
        assert tc.correct()
    make_sample_test(main_sample_cases, 'main')


def board_random_numbers(N):
    A = [random.randint(1, TestCase.max_A) for i in range(N)]
    return A


primes = []


def sieve():
    bs = [True] * (1 + TestCase.max_A)
    global primes
    bs[0] = bs[1] = False
    for i in range(2, len(bs)):
        if bs[i]:
            j = i * i
            while j < len(bs):
                bs[j] = False
                j += i
            primes.append(i)


def board_distributed_primes(N):
    def distributed_number():
        global primes
        number = 1
        while True:
            j = bisect_right(primes, TestCase.max_A // number)
            if j == 0:
                break
            idx = random.randint(0, j - 1)
            number *= primes[idx]
        return number

    A = [distributed_number() for i in range(N)]
    return A


def board_small_primes(N):
    def small_number():
        global primes
        number = 1
        while True:
            j = bisect_right(primes, TestCase.max_A // number)
            if j == 0:
                break
            idx = random.randint(0, min(50, j - 1))
            number *= primes[idx]
        return number
    A = [small_number() for i in range(N)]
    return A


def board_different_primes(N):
    global primes
    return [primes[i % len(primes)] for i in range(N)]

def games_random(N, M):
    G = []
    for i in range(M):
        L, R = random.randint(1, N), random.randint(1, N)
        if L > R:
            L, R = R, L
        G.append([L, R])
    return G

def games_kill_left(N, M):
    left_indices = [random.randint(1, N) for i in range(M)]
    left_indices = sorted(left_indices)
    right_indices = []
    for i in range(M):
        possibles = N - left_indices[i]
        right = (left_indices[i] +
                 (random.randint(0, possibles // 2) if i % 2 == 0 else random.randint(possibles // 2, possibles)))
        right_indices.append(right)
    G = [[left_indices[i], right_indices[i]] for i in range(M)]
    random.shuffle(G)
    return G

def games_kill_right(N, M):
    G = games_kill_left(N, M)
    for i in range(M):
        left = N + 1 - G[i][1]
        right = N + 1 - G[i][0]
        G[i] = [left, right]
    return G


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    
    TODO Write sample tests. Consider creating edge cases and large randomized
    tests.
    """
    sieve()
    print('here')
    for number_generation_type in [board_random_numbers, board_distributed_primes, board_small_primes, board_different_primes]:
        print(number_generation_type.__name__)
        for games_generation_type in [games_random, games_kill_left, games_kill_right]:
            print(games_generation_type.__name__)
            for min_N in [9 * TestCase.max_N // 10, TestCase.max_N]:
                for min_M in [9 * TestCase.max_M // 10, TestCase.max_M]:
                    N = random.randint(min_N, TestCase.max_N)
                    M = random.randint(min_M, TestCase.max_M)
                    A = number_generation_type(N)
                    G = games_generation_type(N, M)
                    main_random_cases = [
                        TestCase(N, M, A, G)
                    ]  # Only one test case since it has high constant factor
                    for tc in main_random_cases:
                        assert tc.correct()
                    make_secret_test(
                        main_random_cases,
                        f'random_cases_{number_generation_type.__name__}_{games_generation_type.__name__}'
                    )
                    print('done')


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    
    TODO Implement this for your problem.
    """
    # Assume that it's only one case
    # TODO Change if we don't like this
    # T = len(cases)
    # print(T, file=file)
    for case in cases:
        print(f'{case.N} {case.M}', file=file)
        print(*case.A, file=file)
        for g in case.G:
            print(*g, file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    
    TODO Implement this for your problem by changing the import below.
    """

    from submissions.accepted.cousins_mo import solve
    for case in cases:
        solve(case.N, case.M, case.A, case.G, file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
