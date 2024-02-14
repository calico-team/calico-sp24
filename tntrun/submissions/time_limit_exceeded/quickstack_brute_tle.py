def solve(N: int, M: int, P: list[str], C: list[str]):
    """
    For every element in the player's list and for every element in the 
    chest's list, it finds an appropiate spot in the new list to insert 
    the element such that duplicate elements are adjacent.
    """
    new_chest = []

    for char in P:
        added = False
        for i in range(len(new_chest)):
            if char == new_chest[i]:
                added = True 
                new_chest.insert(i, char)
                break
        if not added: new_chest.append(char)

    for char in C:
        added = False
        for i in range(len(new_chest)):
            if char == new_chest[i]:
                added = True 
                new_chest.insert(i, char)
                break
        if not added: new_chest.append(char)
    
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

