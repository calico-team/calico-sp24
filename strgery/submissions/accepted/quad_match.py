def solve(A: str, B: str) -> str:
    """
    slow sol
    """
    n = len(A)
    m = len(B)
    # TODO: add testcases of off by 1
    for i in range(1, m):
        s1 = A.find(B[:i])
        if s1 != -1 and s1+i < n:
            s2 = A[s1+i:].find(B[i:])
            if s2 != -1:
                return f"{s1} {i} {s2+s1+i} {m-i}"

    for i in range(1, m):
        s1 = A.find(B[i:])
        l1 = m-i
        # print(i, s1)
        if s1 != -1 and s1+l1 < n:
            s2 = A[s1+l1:].find(B[:i])
            # print(s2)
            if s2 != -1:
                return f"{s2+s1+l1} {i} {s1} {l1}"

    return "IMPOSSIBLE"

def main():
    # print(max_matching_prefix("abcde", "cd"))
    T = int(input())
    for _ in range(T):
        A = input()
        B = input()
        print(solve(A, B))


if __name__ == '__main__':
    main()
