def solve(N: int, K: int, S: str) -> int:
    """
    Return the maximum number of players that can make it across the TNT run.
    If infinitely many players can complete the course, return -1.
    
    N: number of blocks in the course
    K: maximum jump distance of every player
    S: description of the TNT run
    """
    # Idea: calculate the maximum number of air blocks in a segment of K + 1 consecutive blocks, since that is a bottleneck
    if K >= N:
        return -1
    mx, cur = 0, 0
    K += 1
    for i in range(K):
        if S[i] == '-':
            cur += 1
        mx = max(mx, cur)
    for i in range(K, N):
        if S[i] == '-':
            cur += 1
        if S[i - K] == '-':
            cur -= 1
        mx = max(mx, cur)
    return K - mx


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        N, K = int(temp[0]), int(temp[1])
        S = input()
        print(solve(N, K, S))


if __name__ == '__main__':
    main()
