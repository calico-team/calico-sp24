def solve(N: int, M: int, P: list[str], C: list[str]):
    """
    Output a possible configuration of the chest after performing quickstack

    N: the number of items the player has
    M: the number of items the chest has
    P: the list of items on the player
    C: the list of items in the chest
    """
    # YOUR CODE HERE
    return


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