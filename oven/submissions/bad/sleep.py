import time

def solve(D: int, A: str) -> int:
    time.sleep(10 ** 9)
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
