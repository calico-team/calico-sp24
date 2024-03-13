def solve(A: str, B: str) -> str:
    """
    if length is small, brute force
    otherwise, try to match the first 100. Then, match the longest B in
    that position. Then match the rest of B.
    """
    if len(B) < 500:
        for i in range(len(B)):
            if B[:i] in A and B[i:] in A:
                return f"{A.find(B[:i])} {i} {A.find(B[i:])} {len(B)-i}"
        return "-1"

    n = len(B)
    if B[:100] in A:
        pos = A.find(B[:100])
        i = 0
        while i < n:
            if pos+i>=len(A) or A[pos+i] != B[i]: break
            i+=1

        return f"{A.find(B[:100])} {i} {A.find(B[i:i+100])} {n-i}"
    return "-1"


def main():
    T = int(input())
    for _ in range(T):
        A = input()
        B = input()
        print(solve(A, B))


if __name__ == '__main__':
    main()
