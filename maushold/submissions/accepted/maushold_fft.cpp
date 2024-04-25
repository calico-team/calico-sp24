#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const ll MOD = 998244353;

/**
 * Description: modular arithmetic operations.
 *              Not really needed but really convenient so the code is more legible.
 * Source: https://github.com/bqi343/cp-notebook/blob/master/Implementations/content/number-theory%20(11.1)/Modular%20Arithmetic/ModInt.h
 */

template<int MOD, int RT> struct mint {
	static const int mod = MOD;
	static constexpr mint rt() { return RT; } // primitive root for FFT
	int v; explicit operator int() const { return v; } // explicit -> don't silently convert to int
	mint():v(0) {}
	mint(ll _v) { v = int((-MOD < _v && _v < MOD) ? _v : _v % MOD);
		if (v < 0) v += MOD; }
	bool operator==(const mint& o) const {
		return v == o.v; }
	friend bool operator!=(const mint& a, const mint& b) { 
		return !(a == b); }
	friend bool operator<(const mint& a, const mint& b) { 
		return a.v < b.v; }
   
	mint& operator+=(const mint& o) { 
		if ((v += o.v) >= MOD) v -= MOD; 
		return *this; }
	mint& operator-=(const mint& o) { 
		if ((v -= o.v) < 0) v += MOD; 
		return *this; }
	mint& operator*=(const mint& o) { 
		v = int((ll)v*o.v%MOD); return *this; }
	mint& operator/=(const mint& o) { return (*this) *= inv(o); }
	friend mint pow(mint a, ll p) {
		mint ans = 1; assert(p >= 0);
		for (; p; p /= 2, a *= a) if (p&1) ans *= a;
		return ans; }
	friend mint inv(const mint& a) { assert(a.v != 0); 
		return pow(a,MOD-2); }
		
	mint operator-() const { return mint(-v); }
	mint& operator++() { return *this += 1; }
	mint& operator--() { return *this -= 1; }
	friend mint operator+(mint a, const mint& b) { return a += b; }
	friend mint operator-(mint a, const mint& b) { return a -= b; }
	friend mint operator*(mint a, const mint& b) { return a *= b; }
	friend mint operator/(mint a, const mint& b) { return a /= b; }
};

using mi = mint<MOD, 5>;

/**
 * Description: FFT
 * Time: $O(N\log N)$. For $N=10^6$, conv \tilde 0.13ms, conv\_general \tilde 320ms.
 * Source: https://github.com/bqi343/cp-notebook/blob/master/Implementations/content/numerical/Polynomials/FFT.h
 */

template<class T>
void fft(vector<T>& A, bool invert = 0) { // NTT
    int n = A.size();
    assert((T::mod - 1) % n == 0);
    vector<T> B(n);
    for (int b = n / 2; b; b >>= 1, swap(A, B)) { // w = n/b-th root
        T w = pow(T::rt(), (T::mod - 1) / n * b), m = 1;
        for (int i = 0; i < n; i += b * 2, m *= w) {
            for (int j = 0; j < b; ++j) {
                T u = A[i + j], v = A[i + j + b] * m;
                B[i / 2 + j] = u + v;
                B[i / 2 + j + n / 2] = u - v;
            }
        }
    }
    if (invert) {
        reverse(1 + A.begin(), A.end());
        T z = inv(T(n));
        for (auto& t : A) t *= z;
    }
} // for NTT-able moduli

template <class T>
vector<T> conv(vector<T> A, vector<T> B) {
    if (min(A.size(), B.size()) == 0) return {};
    int s = int(A.size()) + int(B.size()) - 1, n = 1;
    for (; n < s; n <<= 1);
    A.resize(n), fft(A);
    B.resize(n), fft(B);
    for (int i = 0; i < n; ++i) A[i] *= B[i];
    fft(A, 1); A.resize(s); return A;
}

void mult(vector<mi>& A, vector<mi>& B, int HP) {
    A = conv(A, B);
    for (int i = HP + 1; i < int(A.size()); ++i)
        A[HP] += A[i];
    A.resize(HP + 1);
}

vector<mi> binpow(vector<mi> A, int HP, ll b) {
    vector<mi> res(HP + 1);
    res[0] = 1;
    while (b) {
        if (b & 1) mult(res, A, HP);
        mult(A, A, HP);
        b >>= 1;
    }
    return res;
}

/**
 * Return the probability of your Pokemon fainting after being hit with Population Bomb.
 * If the probability is p/q, return p * q^-1 mod 1000000007
 * 
 * H: Your Pokemon's HP
 * N: Number of times that Population Bomb hits
 * M: Number of damage rolls
 * R: List of the M damage rolls
 */
int solve(int H, ll N, int M, vector<int> const& R) {
    vector<mi> A(H + 1);
    mi prob = mi(1) / mi(M);
    for (int i = 0; i < M; ++i)
        A[min(H, R[i])] += prob;
    A = binpow(A, H, N);
    return A[H].v;
}

int main() {
    int H, M; ll N;
    cin >> H >> N >> M;
    vector<int> R(M);
    for (int j = 0; j < M; ++j)
        cin >> R[j];
    cout << solve(H, N, M, R) << '\n';
    return 0;
}
