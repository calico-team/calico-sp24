#include <iostream>
#include <string>

using namespace std;

int solve(int N, int K, string S) {
    if (K >= N) return -1;
    ++K;
    int mx = 0, cur = 0;
    for (int i = 0; i < K; ++i) {
        if (S[i] == '-') ++cur;
        mx = max(mx, cur);
    }
    for (int i = K; i < N; ++i) {
        if (S[i] == '-') ++cur;
        if (S[i - K] == '-') --cur;
        mx = max(mx, cur);
    }
    return K - mx;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, K;
        cin >> N >> K;
        string S;
        cin >> S;
        cout << solve(N, K, S) << '\n';
    }
}
