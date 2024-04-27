MOD = 998244353
RT = 62


class mint:
    def __init__(self, v=0, mod=MOD, rt=RT):
        self.v = v % mod
        self.mod = mod
        self.rt = rt

    def __add__(self, other):
        assert self.mod == other.mod
        return mint(self.v + other.v, self.mod, self.rt)

    def __sub__(self, other):
        assert self.mod == other.mod
        return mint(self.v - other.v, self.mod, self.rt)

    def __mul__(self, other):
        assert self.mod == other.mod
        return mint(self.v * other.v, self.mod, self.rt)

    def __truediv__(self, other):
        return self * self.inv(other)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.v)

    def inv(self, a):
        return mint(pow(a.v, self.mod - 2, self.mod), self.mod, self.rt)


def fft(A: list[mint], invert=False):
    """ Number Theoretic Transform """
    T = mint(v=0, mod=A[0].mod, rt=A[0].rt)
    n = len(A)
    assert (T.mod - 1) % n == 0
    B = [T for _ in range(n)]
    b = n // 2
    while b != 0:
        w = mint(pow(T.rt, (T.mod - 1) // n * b, T.mod), T.mod, T.rt)
        m = mint(1, T.mod, T.rt)
        i = 0
        while i < n:
            for j in range(b):
                u = A[i + j]
                v = A[i + j + b] * m
                B[i // 2 + j] = u + v
                B[i // 2 + j + n // 2] = u - v
            i += b * 2
            m = m * w
        b //= 2
        A, B = B, A

    if invert:
        A[1:len(A)] = A[1:len(A)][::-1]
        z = mint(1, T.mod, T.rt) / mint(n, T.mod, T.rt)
        A = [t * z for t in A]

    return A


def conv(A: list[mint], B: list[mint]) -> list[mint]:
    if min(len(A), len(B)) == 0:
        return []
    s, n = len(A) + len(B) - 1, 1
    while n < s:
        n *= 2
    while len(A) < n:
        A.append(mint(v=0, mod=A[0].mod, rt=A[0].rt))
    A = fft(A)
    while len(B) < n:
        B.append(mint(v=0, mod=B[0].mod, rt=B[0].rt))
    B = fft(B)
    for i in range(n):
        A[i] = A[i] * B[i]
    A = fft(A, True)
    return A[:s]


def mul_mod(x: list[mint], y: list[mint], M: mint) -> list[mint]:
    def con(v: list[mint]):
        """ Changes v to be of the class of M """
        return [mint(x.v, M.mod, M.rt) for x in v]

    return conv(con(x), con(y))


def mult(A: list[mint], B: list[mint], HP: int) -> list[mint]:
    A = mul_mod(A, B, mint(mod=(119 <<23) + 1, rt=62))
    for i in range(HP + 1, len(A)):
        A[HP] += A[i]
    return A[:HP + 1]


def binpow(A: list[mint], HP: int, b: int) -> list[mint]:
    res: list[mint] = [mint() for _ in range(HP + 1)]
    res[0] = mint(v=1)
    while b != 0:
        if b % 2 == 1:
            res = mult(res, A, HP)
        A = mult(A, A, HP)
        b //= 2
    return res


def solve(H: int, N: int, M: int, R: list[int]) -> int:
    """
    Return the probability of your Pokemon fainting after being hit with Population Bomb
    If the probability is p/q, return p * q^-1 mod 1000000007

    H: Your Pokemon's HP
    N: Number of times that Population Bomb hits
    M: Number of damage rolls
    R: List of M damage rolls
    """
    A = [mint() for _ in range(H + 1)]
    prob = mint(v=1) / mint(v=M)
    for i in range(M):
        A[min(H, R[i])] = A[min(H, R[i])] + prob
    A = binpow(A, H, N)
    return A[H].v


def main():
    H, N, M = [int(x) for x in input().split()]
    R = [int(x) for x in input().split()]
    print(solve(H, N, M, R))


if __name__ == '__main__':
    main()
