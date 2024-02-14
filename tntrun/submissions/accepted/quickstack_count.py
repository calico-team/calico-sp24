from collections import Counter

def solve(N: int, M: int, P: list[str], C: list[str]):
    """
    Uses a hashmap which maps characters to their frequencies in both the 
    player's list and the chest's list. To construct the new list where 
    duplicate elements are adjacent, iterate over the hashmap's characters
    and re-add them according to their corresponding frequencies.
    """
    char_counts = Counter(C)
    char_counts.update(P)
    new_chest = []
    for char in char_counts:
        for _ in range(char_counts[char]):
            new_chest.append(char)
    print(*new_chest)


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

