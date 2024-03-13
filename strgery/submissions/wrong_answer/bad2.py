from submissions.accepted import n_cube
def solve(A: str, B: str) -> str:
    """
    if length is small, brute force
    otherwise, do bad match linear time match
    """
    if len(B) < 500:
        return n_cube.solve(A, B)

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
