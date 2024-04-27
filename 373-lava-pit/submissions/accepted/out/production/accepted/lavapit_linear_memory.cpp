#include <bits/stdc++.h>
using namespace std;

const int INF = 1E8;

struct Solution {
    int yes, no, row, col, used;
    // dp[i][j] will be the maximum number of diamonds that Steve can pick in the rectangle [0,i] x [0,j] if...
    // yes -> the water bucket is used in block (x, y) = (i, j)
    // no -> the water bucket is not used at all
    // row -> the water bucket is used in block (x, y) with x = i, y < j
    // col -> the water bucket is used in block (x, y) with x < i, y = j
    // used -> the water bucket is used in block (x, y) with x < i, y < j
};

/**
 * Return the maximum number of diamonds that Steve can mine before exiting the lava pit.
 * 
 * N: number of rows in the lava pit
 * M: number of columns in the lava pit
 * G: description of the lava pit
 */
int solve(int N, int M, vector<string> G) {

    vector<Solution> dp(M, {-INF, -INF, -INF, -INF, -INF});

    auto calculate_state = [&](int i, int j) -> void {
        int yes = -INF, no = -INF, row = -INF, col = -INF, used = -INF;
        if (i != 0) {  // What if we come from (i - 1, j)
            yes = max(
                yes,
                dp[j].no
            );
            no = max(
                no,
                G[i][j] == 'L' ? -INF : dp[j].no
            );
            col = max(
                col,
                max(dp[j].col, dp[j].yes)
            );
            used = max(
                used,
                G[i][j] == 'L' ? -INF : max(
                    dp[j].used,
                    dp[j].row
                )
            );
        }

        if (j != 0) { // What if we come from (i, j - 1)
            yes = max(
                yes,
                dp[j - 1].no
            );
            no = max(
                no,
                G[i][j] == 'L' ? -INF : dp[j - 1].no
            );
            row = max(
                row,
                max(dp[j - 1].yes, dp[j - 1].row)
            );
            used = max(
                used,
                G[i][j] == 'L' ? -INF : max(
                    dp[j - 1].col,
                    dp[j - 1].used
                )
            );
        }

        if (G[i][j] == 'D') {  // Really don't care if it's impossible since 1 - INF = -INF
            ++yes;
            ++no;
            ++row;
            ++col;
            ++used;
        }

        dp[j] = { yes, no, row, col, used };

    };

    if (G[0][0] == 'L') {
        dp[0].yes = 0;
    } else if (G[0][0] == 'D') {
        dp[0].yes = dp[0].no = 1;
    } else {
        dp[0].yes = dp[0].no = 0;
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (i || j) calculate_state(i, j);
        }
    }

    Solution ans = dp[M - 1];
    return max({ans.yes, ans.no, ans.row, ans.col, ans.used});

}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N, M;
        cin >> N >> M;
        vector<string> G(N);
        for (int i = 0; i < N; ++i) {
            cin >> G[i];
        }
        int answer = solve(N, M, G);
        if (answer >= 0) {
            cout << answer << '\n';
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }
}
