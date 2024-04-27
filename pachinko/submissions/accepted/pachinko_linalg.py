import numpy as np
from numpy.linalg import linalg

M = 1000


def solve(N: int, S: int, E: int, P: list[int]) -> int:
    """
    Return the expected length of a path that starts at node 1 in the pachinko.

    N: number of nodes in the pachinko
    S: starting node of the flipper
    E: ending node of the flipper
    P: list of parent nodes in the pachinko
    """
    P = [u - 1 for u in P]
    S -= 1
    E -= 1
    g = [list() for _ in range(N)]
    # Build M copies of the tree
    for i in range(N - 1):
        g[P[i]].append(i + 1)
    g[S].append(E)
    A = [[0 for i in range(N)] for i in range(N)]
    b = [0 for i in range(N)]
    for i in range(N):
        A[i][i] = 1
        for j in g[i]:
            A[i][j] -= 1 / len(g[i])
        b[i] = 1 if g[i] else 0

    return linalg.solve(np.array(A), np.array(b))[0]


def main():
    T = int(input())
    for _ in range(T):
        N, S, E = [int(x) for x in input().split()]
        P = [int(x) for x in input().split()]
        print(solve(N, S, E, P))


if __name__ == '__main__':
    main()
