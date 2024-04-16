from math import floor, log2


class RMQ:
    """
    Implements Range Maximum Query
    Indices in queries are inclusive
    """

    def __init__(self, v):
        self.v = v
        self.jmp = []
        self.jmp.append([i for i in range(len(v))])
        j = 1
        while 1 << j <= len(v):
            self.jmp.append([0 for _ in range(len(v) - (1 << j) + 1)])
            for i in range(len(self.jmp[j])):
                self.jmp[j][i] = self.cmb(self.jmp[j - 1][i], self.jmp[j - 1][i + (1 << (j - 1))])
            j += 1

    def cmb(self, a, b):
        return min(a, b) if self.v[a] == self.v[b] else a if self.v[a] > self.v[b] else b

    def index(self, l, r):
        assert l <= r
        d = int(floor(log2(r - l + 1)))
        return self.cmb(self.jmp[d][l], self.jmp[d][r - (1 << d) + 1])

    def query(self, l, r):
        return self.v[self.index(l, r)]


def compute_prefix_function(s: str) -> list[int]:
    """
    Computes the prefix array of the string s using KMP algorithm
    p[i] = length of the longest string that is prefix and suffix of s[0...i) and is not equal to s[0...i)
    p[0] = -1 arbitrarily
    Time: O(|s|)
    """
    p = [-1]
    for i in range(1, len(s) + 1):
        k = p[-1]
        while k >= 0 and s[k] != s[i - 1]:
            k = p[k]
        p.append(k + 1)
    return p


def solve(P: str, S: str):
    """
    Finds nonempty s1, s2 in S with empty intersection such that s1 + s2 = P
    """
    n, m = len(P), len(S)
    fwd_str = P + "#" + S
    back_str = P[::-1] + "#" + S[::-1]
    fwd_prefix = compute_prefix_function(fwd_str)
    back_prefix = compute_prefix_function(back_str)
    # fwd_important[i] = x means that the prefix of P of length x ends in i (inclusive)
    fwd_important = fwd_prefix[n + 2:]
    # back_important[i] = x means that the suffix of P of length x starts at i (inclusive)
    back_important = back_prefix[n + 2:]
    back_important = back_important[::-1]

    rmq = RMQ(back_important)
    assert m == len(fwd_important)
    for i in range(m):
        if fwd_important[i] == n:
            # Won't add anything since s1, s2 have to be non-empty and the case n - 1 is in i - 1
            continue
        if fwd_important[i] == 0:
            # Can't be non-empty
            continue
        if i + 1 < m:
            # Try the case [... prefix ... suffix ...]
            j = rmq.index(i + 1, m - 1)
            if fwd_important[i] + back_important[j] >= n:
                # Solution found
                print(f'{i - fwd_important[i] + 1} {fwd_important[i]} {j} {n - fwd_important[i]}')
                return
        if i - m + fwd_important[i] >= 0:
            # Try the case [... suffix ... prefix ...]
            j = rmq.index(0, i - m + fwd_important[i])
            if fwd_important[i] + back_important[j] >= n:
                # Solution found
                print(f'{i - fwd_important[i] + 1} {fwd_important[i]} {j} {n - fwd_important[i]}')
                return
    # No solution found
    print('IMPOSSIBLE')
    return


def main():
    # T = int(input())
    # for _ in range(T):
    #     S, P = input().split()
    #     print(solve(S, P))
    solve('calico', 'licoca')


if __name__ == '__main__':
    main()
