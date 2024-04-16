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
    print(fwd_important)
    print(back_important)

    max_prefixes = [0 for _ in range(m)]
    for i in range(1, m):
        max_prefixes[i] = i if back_important[max_prefixes[i - 1]] < back_important[i] else max_prefixes[i - 1]

    max_suffixes = [m - 1 for _ in range(m)]
    for i in range(0, m - 1)[::-1]:
        max_suffixes[i] = i if back_important[max_suffixes[i + 1]] < back_important[i] else max_suffixes[i + 1]

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
            j = max_suffixes[i + 1]
            if fwd_important[i] + back_important[j] >= n:
                # Solution found
                print('here')
                print(i)
                print(f'{i - fwd_important[i] + 1} {fwd_important[i]} {j} {n - fwd_important[i]}')
                return
        if i - m >= 0:
            # Try the case [... suffix ... prefix ...]
            j = max_prefixes[i - m]
            if fwd_important[i] + back_important[j] >= n:
                # Solution found
                print('there')
                print(i)
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
    solve('dfhmfh', 'dfhm')


if __name__ == '__main__':
    main()
