def solve(N: int, S: list[str], E: list[str]):
    """
    Output YES if it is possible for the player to run on the course such that it
    consists of blocks and banned otherwise.

    N: the number of blocks in the course.
    S: the list of starting blocks
    E: the list of ending blocks
    """
    ans = True
    cnt = 0
    for s, e in zip(S, E):
        if s == '-' and e == '#':
            ans = False
        if s == '#' and e == '-':
            # the player stepped on this block
            cnt = 0
        if s == e:
            # the player skipped this block
            cnt += 1
            if cnt > 5:
                ans = False

    if ans:
        return "YES"
    else:
        return "banned"

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = [x for x in input()]
        E = [x for x in input()]
        print(solve(N, S, E))


if __name__ == '__main__':
    main()
