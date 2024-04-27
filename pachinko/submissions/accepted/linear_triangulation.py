from collections import deque


def solve(N: int, S: int, E: int, P: list[int]) -> int:
    """
    Return the expected length of a path that starts at node 1 in the pachinko.

    N: number of nodes in the pachinko
    S: starting node of the flipper
    E: ending node of the flipper
    P: list of parent nodes in the pachinko
    """
    # Want 0-based
    S -= 1
    E -= 1
    P = [u - 1 for u in P]

    g = [[] for i in range(N)]
    for i in range(N - 1):
        g[P[i]].append(i + 1)
    g[S].append(E)
    out = [len(g[i]) for i in range(N)]
    A = [{} for i in range(N)]  # Sparse Matrix A
    b = [0 if out[i] == 0 else 1 for i in range(N)]  # Vector b
    for i in range(N):
        A[i][i] = 1
        for j in g[i]:
            if j not in A[i]:
                A[i][j] = 0
            A[i][j] -= 1 / out[i]

    # Let's try to find the cycle. We just go up from S and try to find E
    cyclic = E == S
    cycle = deque()
    cur = S
    while cur != 0 and not cyclic:
        cur = P[cur - 1]
        cycle.appendleft(cur)
        if cur == E:
            cyclic = True

    # Triangulize A
    if cyclic:
        for i in cycle:
            factor = A[S][i] / A[i][i]
            for j in A[i].keys():
                if j not in A[S]:
                    A[S][j] = 0
                A[S][j] -= factor * A[i][j]
            b[S] -= b[i] * factor

    # Now A is "triangular"

    x = [-1 for _ in range(N)]

    def solve_system(i):
        if x[i] != -1:
            return x[i]
        x[i] = b[i]
        for j in A[i].keys():
            if i != j:
                x[i] -= A[i][j] * solve_system(j)
        x[i] /= A[i][i]
        return x[i]

    return solve_system(0)


def main():
    T = int(input())
    for _ in range(T):
        N, S, E = [int(x) for x in input().split()]
        P = [int(x) for x in input().split()]
        print(solve(N, S, E, P))


if __name__ == '__main__':
    main()
