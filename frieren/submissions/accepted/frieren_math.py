def solve(B: int, L: int, E: int) -> int:
    age_at_first_shower = (E + B) % 50

    if age_at_first_shower > L:
        return 0
    
    years_from_first_shower = L - age_at_first_shower
    return years_from_first_shower // 50 + 1


def main():
    T = int(input())
    for _ in range(T):
        B, L, E = map(int, input().split())
        print(solve(B, L, E))

if __name__ == '__main__':
    main()
