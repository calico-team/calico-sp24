def solve(B: int, L: int, E: int) -> int:
    """
    Return the number of times the given person sees the Era Meteor Shower over the course of their life, it it occurs every fifty years.

    B: the number of years ago when someone was born
    L: the lifespan of that person
    E: the number of years until the next Era Meteor Shower
    """
    total = 0

    relative_born_year = -1 * B

    for relative_year in range(E - 50, relative_born_year - 1, -50):
        if relative_born_year <= relative_year <= relative_born_year + L:
            total += 1
    
    for _ in range(E, relative_born_year + L + 1, 50):
        total += 1
    
    return total


def main():
    T = int(input())
    for _ in range(T):
        B, L, E = map(int, input().split())
        print(solve(B, L, E))

if __name__ == '__main__':
    main()