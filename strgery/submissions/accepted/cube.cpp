#include <iostream>
#include <algorithm>
using namespace std;

/**
 * Print the start positions and lengths of two substrings of S, s1 and s2,
 * such that concatenating s1 and s2 yields to P.
 *
 * S: The string you must find the substrings s1 and s2 in.
 * P: The string you want to make by concatenating.
 */

void solve(string S, string P) {
    int n = S.size();
    int m = P.size();
    for (int i = 1; i < m; i++) {
        int s1 = search(S.begin(), S.end(), P.begin(), P.begin()+i) - S.begin();
        if (s1 + i < n) {
            int s2 = search(S.begin() + s1 + i, S.end(), P.begin()+i, P.end()) - S.begin();
            if (s2 < n) {
                printf("%d %d %d %d\n", s1, i, s2, m-i);
                return;
            }
        }
    }

    for (int i = 1; i < m; i++) {
        int s1 = search(S.begin(), S.end(), P.begin()+i, P.end()) - S.begin();
        int l1 = m-i;
        if (s1 + l1 < n) {
            int s2 = search(S.begin() + s1 + l1, S.end(), P.begin(), P.begin()+i) - S.begin();
            if (s2 < n) {
                printf("%d %d %d %d\n", s2, i, s1, l1);
                return;
            }
        }
    }
    printf("IMPOSSIBLE\n");
    return;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string S, P;
        cin >> S >> P;
        solve(S, P);
    }
}
