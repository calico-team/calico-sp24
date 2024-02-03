#include <bits/stdc++.h>
#include "test_case.cpp"
using namespace std;


#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const ll MOD = 1000000007;

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

template<class M, class T>
vector<M> mulMod(vector<T> const& x, vector<T> const& y) {
    auto con = [](vector<T> const& v) {
        vector<M> w(v.size());
        for (int i = 0; i < int(v.size()); ++i)
            w[i] = (int)v[i];
        return w;
    };
    return conv(con(x), con(y));
} // Arbitrary moduli

template <class T>
vector<T> conv_general(vector<T> const& A, vector<T> const& B) {
    using m0 = mint<(119<<23)+1, 62>; auto c0 = mulMod<m0>(A, B);
    using m1 = mint<(5<<25)+1,   62>; auto c1 = mulMod<m1>(A, B);
    using m2 = mint<(7<<26)+1,   62>; auto c2 = mulMod<m2>(A, B);
    int n = int(c0.size()); vector<T> res(n);
    m1 r01 = inv(m1(m0::mod));
    m2 r02 = inv(m2(m0::mod)), r12 = inv(m2(m1::mod));
    for (int i = 0; i < n; ++i) {
        // a - remainder mod m0::mod, b fixes it mod m1::mod
        int a = c0[i].v, b = ((c1[i] - a) * r01).v,
            c = (((c2[i] - a) * r02 - b) * r12).v;
        // c fixes m2:::mod
        res[i] =(T(c) * m1::mod + b) * m0::mod + a;
    }
    return res;
}

void mult(vector<mi>& A, vector<mi>& B, int HP) {
    A = conv_general(A, B);
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
 * This function should solve the test case AND print it through standard output (cout).
 * 
 * Feel free to implement other methods to solve the problem and maybe use the problem template.
 * 
 * The function should look like the main function for the problem if it only had one test case
 * and it everything was already read.
 * 
 * @todo Implement the test case solver.
 * 
*/
void solve_and_print(TestCase const& tc) {
    int H = tc.H;
    ll N = tc.N;
    int M = tc.M;
    vector<int> R = tc.R;
    vector<mi> A(H + 1);
    mi prob = mi(1) / mi(M);
    for (int i = 0; i < M; ++i)
        A[min(H, R[i])] += prob;
    A = binpow(A, H, N);
    cout << A[H].v << '\n';
}