import sys

SZ = 320
primes = []
bs = []


def sieve():
    global primes
    global bs
    primes = []
    bs = [True] * 3200
    bs[0] = False
    bs[1] = False
    for i in range(2, 3200):
        if bs[i]:
            j = i * i
            while j < 3200:
                bs[j] = False
                j += i
            primes.append(i)


def factorize(x):
    cnt = dict()
    for p in primes:
        if p * p > x:
            break
        while x % p == 0:
            if p not in cnt:
                cnt[p] = 0
            x //= p
            cnt[p] += 1
    if x > 1:
        cnt[x] = 1
    return cnt


def solve(N: int, M: int, A: list[int], G: list[list[int]], file) -> None:
    """
    For each game, output who wins the game in one line

    N: size of the game board
    M: number of different games
    A: game board
    G: description of each game
    """
    if not primes:
        sieve()
    for i in range(M):
        G[i][0] -= 1
        G[i][1] -= 1
        G[i].append(i)
    factors = [factorize(A[i]) for i in range(N)]
    answers = [False] * M
    G = sorted(G, key=lambda query: (query[0] // SZ, query[1] if query[0] // SZ % 2 == 0 else -query[1]))
    cur_l, cur_r, ans = 0, -1, 0
    cnt = dict()

    def update(i, add, aux):
        for prime, power in factors[i].items():
            if prime not in cnt:
                cnt[prime] = 0
            aux = aux ^ cnt[prime]
            cnt[prime] += power * add
            aux = aux ^ cnt[prime]
        return aux

    for q in G:
        while cur_l > q[0]:
            cur_l -= 1
            ans = update(cur_l, 1, ans)
        while cur_l < q[0]:
            ans = update(cur_l, -1, ans)
            cur_l += 1
        while cur_r > q[1]:
            ans = update(cur_r, -1, ans)
            cur_r -= 1
        while cur_r < q[1]:
            cur_r += 1
            ans = update(cur_r, 1, ans)
        answers[q[2]] = (ans != 0)
    for res in answers:
        print("IGNACIO" if res else "COUSIN", file=file)
    return


def main():
    N, M = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    G = []
    for i in range(M):
        G.append([int(x) for x in input().split()])
    solve(N, M, A, G, file=sys.stdout)


if __name__ == '__main__':
    main()
