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
from collections import deque

from calico_lib import make_sample_test, make_secret_test, make_data

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'Soy gay y del PSOE'

from graph_randomizer import *

import sys

sys.setrecursionlimit(10 ** 9)

max_T = 10
max_N = 1_000
max_total_N = 10_000


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.

    TODO Change this to store the relevant information for your problem.
    """

    def __init__(self, N, S=None, E=None, P=None, stability=10):
        assert stability >= 0
        attractability = [ra.expovariate(1) + stability for _ in range(N)]  # young money? more like young nerd

        self.N = N
        if P is None:
            tree = [1]
            tree_attract = [attractability.pop()]
            remaining_nodes = list(range(2, N + 1))
            random.shuffle(remaining_nodes)
            self.P = [-1 for _ in range(N - 1)]

            while remaining_nodes:
                next_node = remaining_nodes.pop()
                parent = random.choices(tree, weights=tree_attract)[0]
                self.P[next_node - 2] = parent
                tree.append(next_node)
                tree_attract.append(attractability.pop())

        else:
            self.P = P

        if S is None:
            # TODO Maybe make this better lol. But making a lot of cases should cover all types of edges.
            self.S = random.randint(1, N)
        else:
            self.S = S

        if E is None:
            if random.randint(0, 9) == 0:
                # Let's add a self loop
                self.E = self.P[random.randint(0, N - 1)]  # This assures that it has at least outdeg > 1
            else:
                self.E = random.randint(1, N)
        else:
            self.E = E

    def is_correct(self):
        if not (1 <= self.N <= max_N):
            return False
        if not (1 <= self.S <= self.N):
            return False
        if not (1 <= self.E <= self.N):
            return False
        if len(self.P) != self.N - 1:
            return False
        if self.E != 1 and self.P[self.E - 2] == self.S:
            return False
        # graph has to be a tree rooted at node 1
        g = [set() for _ in range(self.N + 1)]
        for i in range(len(self.P)):
            if not (1 <= self.P[i] <= self.N):
                return False
            g[self.P[i]].add(i + 2)
        q = deque()
        vis = [False for i in range(self.N + 1)]
        vis[0] = True
        q.append(1)
        vis[1] = True
        while q:
            u = q.popleft()
            for v in g[u]:
                if vis[v]:
                    return False  # not a tree
                vis[v] = True
                q.append(v)
        if not all(vis):
            return False
        # Check that the edge does not make the solution infinity
        vis = [False for i in range(self.N + 1)]
        vis[self.E] = True
        q = deque()
        q.append(self.E)
        simple_cycle = True
        while q:
            u = q.popleft()
            if len(g[u]) > 1 or (u == self.S and len(g[u]) == 1):
                simple_cycle = False
            for v in g[u]:
                vis[v] = True
                q.append(v)

        if simple_cycle and vis[self.S]:
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
        TestCase(5, 4, 3, [1, 2, 1, 4]),
        TestCase(9, 6, 3, [1, 1, 2, 2, 5, 1, 7, 6]),
        TestCase(3, 2, 2, [1, 2]),
        TestCase(3, 2, 1, [1, 2]),
        TestCase(23, 7, 1, [1, 2, 3, 4, 5, 6, 7, 4, 9, 9, 9, 10, 10, 12, 12, 12, 16, 16, 14, 14, 21, 21])
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

    stabilities = [10, 1, 5, 0, 2, 100, 0.5, 0.25]
    for s in stabilities:
        batch = []
        for tc in range(max_T):
            N = random.randint(9 * max_N // 10, max_N)
            batch.append(TestCase(N=N, stability=s))
        make_secret_test(batch, f'main_random_{s}')

    # Make some edge cases (line)
    edging = []
    for i in range(max_T):
        N = random.randint(9 * max_N // 10, max_N)
        P = list(range(1, N))
        S = N - random.randint(1, 3)
        E = random.randint(1, 3)
        extra = min(max_N - N, 3)
        for _ in range(extra):
            P.append(random.randint(1, N))
        N += extra
        edging.append(TestCase(N=N, S=S, E=E, P=P))
    make_secret_test(edging, f'edge_uwu')

    # TODO make other test cases (low chance of really big cycle?)
    # idrk how to kill really trivial sols :(

def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.

    TODO Implement this for your problem.
    """
    T = len(cases)
    print(T, file=file)
    assert 1 <= T <= max_T
    total_N = 0
    for case in cases:
        print(f'{case.N} {case.S} {case.E}', file=file)
        print(*case.P, file=file)
        assert case.is_correct()
        total_N += case.N

    assert total_N <= max_total_N


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.

    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.

    TODO Implement this for your problem by changing the import below.
    """
    from submissions.accepted.linear_triangulation import solve  # already checked that its correct with linalg, so lets use this since its faster
    for case in cases:
        print(solve(case.N, case.S, case.E, case.P), file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
