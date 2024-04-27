def solve(B: int, L: int, E: int) -> int:
    """
    Return the number of times the person saw the Era Meteor Shower if it happens every fifty years

    B: year the person was born
    L: the person's lifespan
    E: year the Demon King was slain and an Era Meteor Shower occurred
    """
    return 0


def main():
    T = int(input())
    for _ in range(T):
        B, L, E = map(int, input().split())
        print(solve(B, L, E))

if __name__ == '__main__':
    main()