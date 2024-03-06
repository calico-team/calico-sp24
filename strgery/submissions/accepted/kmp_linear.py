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
def max_matching_prefix(T, P):
    """ 
    KMP search main algorithm: String -> String -> [Int] 
    Return the maximum matching prefix of pattern string P in T
    """
    p, j = partial(P), 0
    ret = 0
    index = 0

    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = p[j - 1]
        if T[i] == P[j]: j += 1
        if j > ret:
            ret = j
            index = i
        ret = max(ret, j)
        if j == len(P): 
        #     ret.append(i - (j - 1))
            j = p[j - 1]

    return ret, index

def solve(A: str, B: str) -> str:
    """
    linear sol
    """
    pos, i1 = max_matching_prefix(A, B)
    # TODO: add testcases of off by 1
    str2 = B[pos:]
    x, i2 = max_matching_prefix(A, str2)
    if x == len(str2):
        return f"{i1-pos+1} {pos} {i2-len(str2)+1} {len(str2)}"
    return "-1"

def main():
    T = int(input())
    for _ in range(T):
        A = input()
        B = input()
        print(solve(A, B))


if __name__ == '__main__':
    main()
