from collections import deque

MOD = 998244353


def solve(N: int, S: int, E: int, P: list[int]) -> float:
    """
    Return the expected length of a path that starts at node 1 in the pachinko.

    N: number of nodes in the pachinko
    S: starting node of the flipper
    E: ending node of the flipper
    P: list of parent nodes in the pachinko
    """
    # Final graph will have N + 1 nodes. It is weighted and directed
    g = [dict() for _ in range(N + 1)]
    for i in range(len(P)):
        g[P[i]][i + 2] = 1
    g[S][E] = 1

    # Run a DFS on root 1 to find a cycle
    depths = [-1 for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]

    def dfs(u, cnt):
        depths[u] = cnt
        visited[u] = 1
        found_cycle = False
        for v in g[u].keys():
            if visited[v] == 1:
                found_cycle = True
            elif visited[v] == 0:
                if dfs(v, cnt + 1):
                    found_cycle = True
        visited[u] = 2
        return found_cycle

    cyclic = dfs(1, 0)

    if cyclic:
        # We have to add an extra ghost node and edge.
        dist = [1 for i in range(N + 1)]
        q = deque()
        q.append(E)
        while q:
            u = q.popleft()
            d = dist[u]
            for v in g[u].keys():
                if v != E:
                    dist[v] = d / len(g[u])
                    q.append(v)
        k = depths[S] - depths[E] + 1  # length of the cycle
        p = dist[S] / len(g[S])  # calculates the change of staying in the cycle one more time
        # The expected time spent in the cycle is the sum from i = 1 to infinity of k * i * p^i * (1 - p) = k * p * (1 - p)
        x = k * p / (1-p)  # Average time spent in the cycle (geometric sum)
        parent = 0 if E == 1 else P[E - 2]
        g[S].pop(E)
        if parent != 0:
            g[parent].pop(E)
            g[parent][0] = 1
        g[0][E] = x

    # Now the graph is acyclic and we can just calculate the solution by recursion.
    # Note that since it might not be a tree, we have to use memoization

    memo = [-1 for i in range(N + 1)]
    def expected(u):
        """Expected length of path starting from u. It is just sum(expected(v) for v in children(u)) / outdeg(u)"""
        if memo[u] != -1:
            return memo[u]
        ans = 0
        for v, w in g[u].items():
            ans += w + expected(v)
        if g[u]:
            ans /= len(g[u])
        memo[u] = ans
        return ans

    return expected(0 if cyclic and E == 1 else 1)


def main():
    T = int(input())
    for _ in range(T):
        N, S, E = [int(x) for x in input().split()]
        P = [int(x) for x in input().split()]
        print(solve(N, S, E, P))


if __name__ == '__main__':
    main()
