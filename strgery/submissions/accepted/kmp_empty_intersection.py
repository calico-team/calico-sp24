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


def compute_zeta_function(s: str) -> list[int]:
    """
    Computes the zeta function of the string s
    z[i] = max k such that s[0:k-1] == s[i:i+k-1]
    z[0] = 0 arbitrarily, although should be len(s)
    Time: O(|s|)
    """
    z = [0 for _ in range(len(s))]
    l, r = 0, 0
    for i in range(1, len(s)):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


def solve(S: str, P: str):
    """
    Finds nonempty s1, s2 in S with empty intersection such that s1 + s2 = P
    """
    N, M = len(S), len(P)
    T1 = P + '#' + S
    T2 = P[::-1] + '#' + S[::-1]

    # prefix[i] = j means that there is a prefix of P of length j that ends at index i
    prefix = compute_prefix_function(T1)[M + 2:]
    # print(prefix)

    # suffix[i] = j means that there is a suffix of P of length j that starts from index i
    suffix = compute_prefix_function(T2)[M + 2:][::-1]
    # print(suffix)

    # prefix_z[i] = j means that there is a prefix of P of length j that starts from index i
    prefix_z = compute_zeta_function(T1)[M + 1:]
    # print(prefix_z)

    # suffix_z[i] = j means that there is a suffix of P of length j that ends at index i
    suffix_z = compute_zeta_function(T2)[M + 1:][::-1]
    # print(suffix_z)

    right_idx = [N - 1 for i in range(N)]
    for i in range(0, N - 1)[::-1]:
        right_idx[i] = i if suffix[i] > suffix[right_idx[i + 1]] else right_idx[i + 1]

    right_idx_z = [N - 1 for i in range(N)]
    for i in range(0, N - 1)[::-1]:
        right_idx_z[i] = i if prefix_z[i] > prefix_z[right_idx_z[i + 1]] else right_idx_z[i + 1]

    # Test S = [ ... s1 ... s2 ... ]
    for i in range(0, N - 1):
        j = right_idx[i + 1]
        if min(prefix[i], M - 1) + min(suffix[j], M - 1) >= M:
            prefix[i] = min(prefix[i], M - 1)
            j += suffix[j] + prefix[i] - M
            return f'{i - prefix[i] + 1} {prefix[i]} {j} {M - prefix[i]}'

    # Test S = [ ... s2 ... s1 ... ]
    for j in range(0, N - 1):
        i = right_idx_z[j + 1]
        if min(prefix_z[i], M - 1) + min(suffix_z[j], M - 1) >= M:
            prefix_z[i] = min(prefix_z[i], M - 1)
            return f'{i} {prefix_z[i]} {j - (M - prefix_z[i]) + 1} {M - prefix_z[i]}'

    return 'IMPOSSIBLE'


def main():
    T = int(input())
    for _ in range(T):
        S = input()
        P = input()
        print(solve(S, P))


if __name__ == '__main__':
    main()
