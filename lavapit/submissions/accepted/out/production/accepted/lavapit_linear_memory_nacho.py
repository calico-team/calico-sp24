def solve(N: int, M: int, G: list[str]):
    """
    Return the maximum number of diamonds that Steve can mine before exiting the lava pit.

    N: number of rows in the lava pit
    M: number of columns in the lava pit
    G: description of the lava pit
    """

    inf = 10_000_000

    class DpState:
        def __init__(self, no=-inf, yes=-inf, used=-inf, row=-inf, col=-inf):
            # Values are -infinity by default and a value < 0 means that you can't reach that state
            self.no = no  # Never used a bucket
            self.yes = yes  # Used a bucket in this position
            self.used = used  # Used a bucket but not in this row or column
            self.row = row  # Used a bucket somewhere in this row
            self.col = col  # Used a bucket somewhere in this column

    memo = [DpState() for j in range(M)]

    def dp(j: int):
        no, yes, used, row, col = [-inf] * 5
        if i != 0:  # Came from (i - 1, j)
            # use bucket at (x, y) = (i, j)
            yes = max(yes, memo[j].no)
            # never used bucket
            no = max(no, memo[j].no if G[i][j] != 'L' else -inf)
            # used bucket at (x, y) with x < i, y = j
            col = max(col, max(memo[j].col, memo[j].yes))
            # used bucket at (x, y) with x < i and y < j
            used = max(used, max(memo[j].row, memo[j].used) if G[i][j] != 'L' else -inf)

        if j != 0:  # Came from (i, j - 1)
            # use bucket at (x, y) = (i, j)
            yes = max(yes, memo[j - 1].no)
            # never used a bucket
            no = max(no, memo[j - 1].no if G[i][j] != 'L' else -inf)
            # used bucket at (x, y) with x < i and y = j
            row = max(row, max(memo[j - 1].row, memo[j - 1].yes))
            # used bucket at (x, y) with x < i and y < j
            used = max(used, max(memo[j - 1].col, memo[j - 1].used) if G[i][j] != 'L' else -inf)

        diamond = 1 if G[i][j] == 'D' else 0

        memo[j] = DpState(no + diamond, yes + diamond, used + diamond, row + diamond, col + diamond)

    if G[0][0] == 'L':
        memo[0] = DpState(yes=0)
    elif G[0][0] == 'D':
        memo[0] = DpState(yes=1, no=1)
    elif G[0][0] == 'O':
        memo[0] = DpState(yes=0, no=0)

    for i in range(N):
        for j in range(M):
            if i != 0 or j != 0:
                dp(j)

    ans = max([getattr(memo[M - 1], atr) for atr in ['yes', 'no', 'used', 'row', 'col']])

    if ans < 0:
        return 'IMPOSSIBLE'
    else:
        return ans


def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        G = [input() for i in range(N)]
        print(solve(N, M, G))


if __name__ == '__main__':
    main()
