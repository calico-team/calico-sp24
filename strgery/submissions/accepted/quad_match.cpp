// pretty fast n^2 solution
#include <bits/stdc++.h>
using namespace std;

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,popcnt,lzcnt")

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) {
        string s, p;
        cin >> s >> p;
        int n = s.size();
        int m = p.size();

        int x1 = 0;
        int i1 = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i+j >= n || p[j] != s[i+j]) {
                    break;
                }
                if (j+1 > x1) {
                    x1 = j+1;
                    i1 = i;
                }
            }
        }

        int x2 = 0;
        int i2 = 0;
        // cout << x1 << ' ' << i1 << '\n';
        for (int i = 0; i < n; i++) {
            for (int j = 0; j+x1 < m; j++) {
                if (i+j >= n || p[j+x1] != s[i+j]) {
                    break;
                }
                if (j+1 > x2) {
                    x2 = j+1;
                    i2 = i;
                }
            }
        }

        // cout << x2 << ' ' << i2 << '\n';
        if (x1+x2 == m) {
            cout << i1 << ' ' << x1 << ' ' << i2 << ' ' << m-x1 << '\n';
        } else {
            cout << -1 << '\n';
        }
    }

    return 0;
}
