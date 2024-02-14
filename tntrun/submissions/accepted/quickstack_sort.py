def solve(N: int, M: int, P: list[str], C: list[str]):
    """
    Combines the player's list with the chest's list and then sorts 
    the resulting list. Naturally, this makes duplicate elements adjacent 
    to each other.
    """
    C.extend(P)
    C.sort()
    print(*C)


def main():
    T = int(input())
    for _ in range(T):
        info = input().split(' ')
        N, M = int(info[0]), int(info[1])
        P = [x for x in input().split(' ')]
        C = [x for x in input().split(' ')]
        solve(N, M, P, C)


if __name__ == '__main__':
    main()

