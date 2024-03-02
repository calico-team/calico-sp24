def solve(A: str, B: str) -> str:
    '''
    n cubed solution
    '''
    for i in range(len(B)):
        if B[:i] in A and B[i:] in A:
            return "y"
    return "n"


def main():
    T = int(input())
    for _ in range(T):
        A, B = input().split()
        print(solve(A, B))


if __name__ == '__main__':
    main()
