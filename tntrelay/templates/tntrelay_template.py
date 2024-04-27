def solve(N: int, K: int, S: str) -> int:
    """
    Return the number of players who can make it across the course. 
    
    N: Denotes the number of blocks in the course
    K: Which denotes the maximum jump distance of each player
    S: The course represented as a list of strings
    """
    # YOUR CODE HERE
    return 0


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        N, K = int(temp[0]), int(temp[1])
        S = input().split()
        for i in range(len(S)):
            S[i] = int(S[i])
        print(solve(N, K, C))

if __name__ == '__main__':
    main()
