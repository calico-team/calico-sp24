#include <bits/stdc++.h>
using namespace std;

const int SZ = 320;
vector<int> primes;
bitset<3200> bs;

void sieve() {
    bs.set();
    bs[0] = bs[1] = 0;
    for (int i = 2; i < 3200; ++i) if (bs[i]) {
        for (int j = i * i; j < 3200; j += i) bs[j] = 0;
        primes.push_back(i);
    }
}

void factorize(int x, unordered_map<int, int>& cnt) {
    for (int p : primes) {
        if (p * p > x) break;
        while (x % p == 0) {
            ++cnt[p];
            x /= p;
        }
    }
    if (x > 1) cnt[x] = 1;
}

struct cmp {
    bool operator () (vector<int> const& v1, vector<int> const& v2) {
        if (v1[0] / SZ != v2[0] / SZ)
            return v1[0] / SZ < v2[0] / SZ;
        return (v1[0] / SZ & 1) ? (v1[1] < v2[1]) : (v1[1] > v2[1]);
    }
};


/**
 * For each game output who wins the game in one line.
 * 
 * N: size of the game board
 * M: number of different games
 * A: game board
 * G: description of each game
 */
void solve(int N, int M, vector<int>& A, vector<vector<int>>& G) {
    if (primes.empty()) sieve();
    vector<unordered_map<int, int>> factors(N);
    for (int i = 0; i < N; ++i)
        factorize(A[i], factors[i]);
    for (auto& q : G) {
        unordered_map<int, int> cnt;
        for (int i = q[0]; i <= q[1]; ++i) {
            for (auto& me : factors[i]) {
                cnt[me.first] += me.second;
            }
        }
        int ans = 0;
        for (auto& me : cnt) {
            ans ^= me.second;
        }
        cout << (ans != 0 ? "IGNACIO\n" : "COUSIN\n");
    }
}

int main() {

    int N, M;
    cin >> N >> M;
    vector<int> A(N);
    vector<vector<int>> G(M, vector<int>(2));
    for (int i = 0; i < N; ++i)
        cin >> A[i];
    for (int i = 0; i < M; ++i)
        cin >> G[i][0] >> G[i][1];
    solve(N, M, A, G);
    return 0;

}
