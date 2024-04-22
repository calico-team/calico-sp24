def solve(D: int, A: str) -> int:
    x = 1
    for _ in range(10 ** 5):
        x *= 3
    
    if A == 'INCREMENT':
        return D + 1
    elif A == 'DECREMENT':
        return D - 1
    else:
        return D


def main():
    D = int(input())
    A = input()
    print(solve(D, A))


if __name__ == '__main__':
    main()
