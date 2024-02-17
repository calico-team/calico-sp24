#include <iostream>
#include <vector>

using namespace std;

/**
 * Output YES if it is possible for the player to run on the course such that it
 * consists of blocks and banned otherwise.
 * 
 * N: the number of blocks in the course.
 * S: the list of starting blocks
 * E: the list of ending blocks
 */
void solve(int N, vector<char> S, vector<char> E) {
    bool ans = true;
    int cnt = 0;
    for (int i = 0; i < N; i++) {
        if (S[i] == '-' && E[i] == '#') {
            ans = false;
        }
        if (S[i] == '#' && E[i] == '-') {
            cnt = 0;
        }
        if (S[i] == E[i]) {
            cnt += 1;
            if (cnt > 4) {
                ans = false;
            }
        }
    }

    if (ans) {
        cout << "YES" << '\n';
    } else {
        cout << "banned" << '\n';
    }
    return;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        vector<char> S(N);
        for (char &item : S) {
            cin >> item;
        }
        vector<char> E(N);
        for (char &item : E) {
            cin >> item;
        }
        solve(N, S, E);
    }
}
