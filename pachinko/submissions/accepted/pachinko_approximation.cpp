#include <bits/stdc++.h>
using namespace std;

const int M = 100;

/**
 * Return the expected length of a path that starts at node 1 in the pachinko.
 * 
 * N: number of nodes in the pachinko
 * S: starting node of the flipper
 * E: ending node of the flipper
 * P: list of parent nodes in the pachinko
 */
double solve(int N, int S, int E, vector<int> P) {
    // Let's make it 0-based
    --S, --E;
    for (int& p : P) --p;
    vector<vector<int>> g(N);
    for (int i = 0; i < N - 1; ++i) {
        g[P[i]].push_back(i + 1);
    }
    g[S].push_back(E);
    vector<int> visited(N, 0);

    auto expected = [&](int i, auto&& self) -> double {
        if (++visited[i] == M) return 0;
        double ans = 0;
        for (int j : g[i]) {
            ans += self(j, self);
        }
        ans /= double(g[i].size());
        return ans;
    };

    return expected(0, expected);
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N, S, E;
        cin >> N >> S >> E;
        vector<int> P(N - 1);
        for (int i = 0; i < N - 1; ++i) {
            cin >> P[i];
        }
        cout << fixed << setprecision(6) << solve(N, S, E, P) << '\n';
    }
    return 0;
}
