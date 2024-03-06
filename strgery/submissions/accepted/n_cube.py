def solve(A: str, B: str) -> str:
    """
    n cubed solution
    """
    for i in range(len(B)):
        if B[:i] in A and B[i:] in A:
            return f"{A.find(B[:i])} {i} {A.find(B[i:])} {len(B)-i}"
    return "-1"


def main():
    T = int(input())
    for _ in range(T):
        A = input()
        B = input()
        print(solve(A, B))


if __name__ == '__main__':
    main()
