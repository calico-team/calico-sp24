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

    vector<vector<Solution>> dp(N, vector<Solution>(M, {-INF, -INF, -INF, -INF, -INF}));

    auto calculate_state = [&](int i, int j) -> void {
        if (i != 0) {  // What if we come from (i - 1, j)
            dp[i][j].yes = max(
                dp[i][j].yes,
                dp[i - 1][j].no
            );
            dp[i][j].no = max(
                dp[i][j].no,
                G[i][j] == 'L' ? -INF : dp[i - 1][j].no
            );
            dp[i][j].col = max(
                dp[i][j].col,
                max(dp[i - 1][j].col, dp[i - 1][j].yes)
            );
            dp[i][j].used = max(
                dp[i][j].used,
                G[i][j] == 'L' ? -INF : max(
                    dp[i - 1][j].used,
                    dp[i - 1][j].row
                )
            );
        }

        if (j != 0) { // What if we come from (i, j - 1)
            dp[i][j].yes = max(
                dp[i][j].yes,
                dp[i][j - 1].no
            );
            dp[i][j].no = max(
                dp[i][j].no,
                G[i][j] == 'L' ? -INF : dp[i][j - 1].no
            );
            dp[i][j].row = max(
                dp[i][j].row,
                max(dp[i][j - 1].yes, dp[i][j - 1].row)
            );
            dp[i][j].used = max(
                dp[i][j].used,
                G[i][j] == 'L' ? -INF : max(
                    dp[i][j - 1].col,
                    dp[i][j - 1].used
                )
            );
        }

        if (G[i][j] == 'D') {  // Really don't care if it's impossible since 1 - INF = -INF
            ++dp[i][j].yes;
            ++dp[i][j].no;
            ++dp[i][j].row;
            ++dp[i][j].col;
            ++dp[i][j].used;
        }

    };

    if (G[0][0] == 'L') {
        dp[0][0].yes = 0;
    } else if (G[0][0] == 'D') {
        dp[0][0].yes = dp[0][0].no = 1;
    } else {
        dp[0][0].yes = dp[0][0].no = 0;
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (i || j) calculate_state(i, j);
        }
    }

    Solution ans = dp[N - 1][M - 1];
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
