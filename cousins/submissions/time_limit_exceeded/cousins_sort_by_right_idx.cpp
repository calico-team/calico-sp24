#include <bits/stdc++.h>
using namespace std;

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
        if (v1[0] > v2[0]) return true;
        else if (v1[0] == v2[0] && v1[1] > v2[1]) return true;
        return false;
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
    for (int i = 0; i < M; ++i) G[i].push_back(i), --G[i][0], --G[i][1];
    vector<unordered_map<int, int>> factors(N);
    for (int i = 0; i < N; ++i)
        factorize(A[i], factors[i]);
    sort(G.begin(), G.end(), cmp());
    vector<bool> answers(M);
    int cur_l = 0, cur_r = -1, ans = 0;
    unordered_map<int, int> cnt;
    auto update = [&](int i, int add) -> void {
        for (auto& me : factors[i]) {
            ans ^= cnt[me.first];
            cnt[me.first] += me.second * add;
            ans ^= cnt[me.first];
        }
    };
    for (auto& q : G) {
        while (cur_l > q[0]) {
            update(--cur_l, 1);
        }
        while (cur_l < q[0]) {
            update(cur_l++, -1);
        }
        while (cur_r > q[1]) {
            update(cur_r--, -1);
        }
        while (cur_r < q[1]) {
            update(++cur_r, 1);
        }
        answers[q[2]] = (ans != 0);
    }
    for (int i = 0; i < M; ++i) {
        cout << (answers[i] ? "IGNACIO" : "COUSIN") << '\n';
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
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
