# WIP
# https://gist.github.com/m00nlight/daa6786cc503fde12a77
def partial(pattern):
    """ Calculate partial match table: String -> [Int]"""
    ret = [0]

    for i in range(1, len(pattern)):
        j = ret[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = ret[j - 1]
        ret.append(j + 1 if pattern[j] == pattern[i] else j)
    return ret

# IDK how kmp works i think this is correct
def has_match(T, P, find_last=False):
    """ 
    KMP search main algorithm: String -> String -> [Int]
    Return the a list where v[i] = maximum matching prefix
    of pattern string P in T[:i]
    """
    p, j = partial(P), 0
    ret = -1
    if P == '':
        assert False

    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = p[j - 1]
        if T[i] == P[j]: j += 1
        # j is the length of the longest prefix in P that matches the end of T[:i+1]
        if j == len(P):
            if not find_last:
                return i+1
            ret = i+1
        if j == len(P): 
            j = p[j - 1]
    return ret

def solve(S: str, P: str) -> str:
    """
    n^2 sol
    """
    n = len(S)
    m = len(P)
    for i in range(1, m):
        pos = has_match(S, P[:i])
        pos2 = has_match(S, P[i:], True)
        if pos != -1 and pos2 != -1 and pos <= pos2-(m-i):
            return f"{pos-i} {i} {pos2-(m-i)} {m-i}"
        pos = has_match(S, P[:i], True)
        pos2 = has_match(S, P[i:])
        # print(i, pos, pos2)
        if pos != -1 and pos2 != -1 and pos2 <= pos-i:
            return f"{pos-i} {i} {pos2-(m-i)} {m-i}"
    return "IMPOSSIBLE"

def main():
    # print(max_matching_prefix('aaaaa', 'aaaaa'))

    T = int(input())
    for _ in range(T):
        A = input()
        B = input()
        print(solve(A, B))


if __name__ == '__main__':
    main()
