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
    // The final graph will have N + 1 nodes. It is weighted and directed.
    vector<unordered_map<int, double>> g(N + 1);
    for (int i = 0; i < N - 1; ++i) {
        g[P[i]][i + 2] = 1;
    }
    g[S][E] = 1;

    // Run a DFS on root 1 to find a cycle.
    vector<int> depths(N + 1, -1);
    vector<int> visited(N + 1);

    auto dfs = [&](int u, int cnt, auto&& self) -> bool {
        depths[u] = cnt;
        visited[u] = 1;
        bool found_cycle = false;
        for (auto& v : g[u]) {
            if (visited[v.first] == 1)
                found_cycle = true;
            else if (!visited[v.first] && self(v.first, cnt + 1, self))
                found_cycle = true;
        }
        visited[u] = 2;
        return found_cycle;
    };

    bool cyclic = dfs(1, 0, dfs);

    if (cyclic) {
        // We have to add an extra ghost node and edge
        vector<double> dist(N + 1, 1);
        queue<int> q;
        q.push(E);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            double d = dist[u];
            for (auto& v : g[u]) {
                if (v.first != E) {
                    dist[v.first] = d / double(g[u].size());
                    q.push(v.first);
                }
            }
        }
        double k = depths[S] - depths[E] + 1; // lenght of the cycle
        double p = dist[S] / double(g[S].size()); // product of all outdegrees in the path
        // The expected time spent in the cycle is the sum from i = 1 to infinity of k * i * p^i * (1 - p) = k * p * (1 - p)
        double x = k * p / (1 - p); // Average time spent doing full cycles
        int parent = (E == 1 ? 0 : P[E - 2]);
        g[S].erase(E);
        if (parent) {
            g[parent].erase(E);
            g[parent][0] = 1;
        }
        g[0][E] = x;
    }

    // Now the graph is acyclic and we can just calculate the solution by recursion
    // NOte that since it might not be a tree now, we have to use memoization
    vector<double> memo(N + 1, -1);

    auto expected = [&](int u, auto&& self) -> double {
        // Expected length of path starting from u. It is just sum(expected(v) for v in children(u)) / outdeg(u)
        double& ans = memo[u];
        if (ans != -1) return ans;
        ans = 0;
        for (auto& me : g[u]) {
            ans += self(me.first, self) + me.second;
        }
        if (!g[u].empty()) ans /= double(g[u].size());
        return ans;
    };

    return expected(!(cyclic && E == 1), expected);

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
