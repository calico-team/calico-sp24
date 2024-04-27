def solve(B: int, L: int, E: int) -> int:
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
