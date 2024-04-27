def solve(Y: int, L: int, D: int) -> int:
    """
    Return the number of times the person saw the Era Meteor Shower if it happens every fifty years

    Y: year the person was born
    L: the person's lifespan
    D: year the Demon King was slain and an Era Meteor Shower occurred
    """
    return 0


def main():
    T = int(input())
    for _ in range(T):
        Y, L, D = map(int, input().split())
        print(solve(Y, L, D))

if __name__ == '__main__':
    main()