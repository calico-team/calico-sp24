#include <bits/stdc++.h>
using namespace std;

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
    vector<int> out(N);
    for (int i = 0; i < N; ++i) {
        out[i] = int(g[i].size());
    }
    vector<unordered_map<int, double>> A(N); // Sparse matrix A
    vector<double> b(N); // Vector b
    for (int i = 0; i < N; ++i) {
        A[i][i] = 1;
        for (int j : g[i]) {
            A[i][j] -= double(1) / double(out[i]);
        }
    }
    for (int i = 0; i < N; ++i) {
        b[i] = g[i].empty() ? 0 : 1;
    }

    // Let's try to find the cycle. We just go up from S and try to find E.
    bool cyclic = E == S;
    stack<int> cycle;
    int cur = S;
    while (cur != 0 && !cyclic) {
        cur = P[cur - 1];
        cycle.push(cur);
        if (cur == E) {
            cyclic = true;
        }
    }

    // Triangulize A
    if (cyclic) {
        while (!cycle.empty()) {
            int i = cycle.top(); cycle.pop();
            double factor = A[S][i] / A[i][i];
            for (auto& me : A[i]) {
                A[S][me.first] -= factor * me.second;
            }
            b[S] -= b[i] * factor;
        }
    }

    // Now A is triangular for some order of indices
    vector<double> x(N, -1); // Ax = b

    auto solve_system = [&](int i, auto&& self) -> double {
        if (x[i] != -1) return x[i];
        x[i] = b[i];
        for (auto& me : A[i]) {
            if (i != me.first) {
                x[i] -= me.second * self(me.first, self);
            }
        }
        x[i] /= A[i][i];
        return x[i];
    };

    return solve_system(0, solve_system);

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
