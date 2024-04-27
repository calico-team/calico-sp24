def solve(B: int, L: int, E: int) -> int:
    """
    Return the number of times the person saw the Era Meteor Shower if it happens every fifty years

    Y: year the person was born
    L: the person's lifespan
    D: year the Demon King was slain and an Era Meteor Shower occurred
    """
    born = (B - E) % 50
    death = (born + L) % 50
    return L // 50 + (1 if death <= born else 0)


def main():
    T = int(input())
    for _ in range(T):
        B, L, E = map(int, input().split())
        print(solve(B, L, E))

if __name__ == '__main__':
    main()
