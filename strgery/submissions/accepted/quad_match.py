def max_matching_prefix(T, P):
    """ 
    Same has linear solution, but use naive matching
    """
    ret = 0
    index = 0
    for i in range(len(T)):
        for j in range(len(P)):
            if i+j >= len(T) or P[j] != T[i+j]:
                break
            if j+1 > ret:
                ret = j+1
                index = i

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
        return f"{i1} {pos} {i2} {len(str2)}"
    return "-1"

def main():
    # print(max_matching_prefix("abcde", "cd"))
    T = int(input())
    for _ in range(T):
        A = input()
        B = input()
        print(solve(A, B))


if __name__ == '__main__':
    main()
