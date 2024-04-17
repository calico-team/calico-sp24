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


def solve(S: str, P: str):
    """
    Finds nonempty s1, s2 in S with empty intersection such that s1 + s2 = P
    """
    N, M = len(S), len(P)
    T1 = P + '#' + S
    T2 = P[::-1] + '#' + S[::-1]
    # prefix[i] = j means that there is a prefix of P of length j that ends at index i
    prefix = compute_prefix_function(T1)[M + 2:]
    # suffix[i] = j means that there is a suffix of P of length j that starts from index i
    suffix = compute_prefix_function(T2)[M + 2:][::-1]

    left_idx = [0 for _ in range(N)]
    for i in range(1, N):
        left_idx[i] = i if suffix[i] > suffix[left_idx[i - 1]] else left_idx[i - 1]
    right_idx = [N - 1 for i in range(N)]
    for i in range(0, N - 1)[::-1]:
        right_idx[i] = i if suffix[i] > suffix[right_idx[i + 1]] else right_idx[i + 1]

    def check(i, j):
        # Tries to build the solution with s1 ending at i and s2 starting at j
        return min(prefix[i], M - 1) + min(suffix[j], M - 1) >= M

    def build_sol(i, j):
        # Tries to build the solution with s1 ending at i and s2 starting at j
        prefix[i] = min(prefix[i], M - 1)
        j += suffix[j] + prefix[i] - M
        return f'{i - prefix[i] + 1} {prefix[i]} {j} {M - prefix[i]}'

    # Test S = [ ... s1 ... s2 ... ]
    for i in range(0, N - 1):
        if check(i, right_idx[i + 1]):
            return build_sol(i, right_idx[i + 1])

    # Test S = [ ... s2 ... s1 ... ]
    for i in range(M - 1, N):
        if check(i, left_idx[i - M + 1]):
            return build_sol(i, left_idx[i - M + 1])

    return 'IMPOSSIBLE'


def main():
    T = int(input())
    for _ in range(T):
        S = input()
        P = input()
        print(solve(S, P))


if __name__ == '__main__':
    main()
