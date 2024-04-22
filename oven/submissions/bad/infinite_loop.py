def solve(D: int, A: str) -> int:
    if D < 50:
        if A == 'INCREMENT':
            return D + 1
        elif A == 'DECREMENT':
            return D - 1
        else:
            return D
    else:
        x = 1
        while True:
            x *= 3


def main():
    D = int(input())
    A = input()
    print(solve(D, A))


if __name__ == '__main__':
    main()
