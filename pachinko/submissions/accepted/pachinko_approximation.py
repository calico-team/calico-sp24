from collections import deque

M = 100


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
    g = [list() for _ in range(N * M)]
    # Build M copies of the tree
    for j in range(M):
        for i in range(N - 1):
            g[N * j + P[i]].append(N * j + i + 1)
    # Build M - 1 copies of the flipper
    for j in range(M - 1):
        g[N * j + S].append(N * (j + 1) + E)

    # Toposort
    topo = []
    q = deque()
    indeg = [0 for i in range(len(g))]
    for u in range(len(g)):
        for v in g[u]:
            indeg[v] += 1
    for u in range(len(indeg)):
        if indeg[u] == 0:
            q.append(u)

    while q:
        u = q.popleft()
        topo.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    answers = [0 for i in range(len(topo))]

    for u in topo[::-1]:
        for v in g[u]:
            answers[u] += 1 + answers[v]
        if g[u]:
            answers[u] /= len(g[u])

    return answers[0]


def main():
    T = int(input())
    for _ in range(T):
        N, S, E = [int(x) for x in input().split()]
        P = [int(x) for x in input().split()]
        print(solve(N, S, E, P))


if __name__ == '__main__':
    main()
