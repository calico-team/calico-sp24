#include <iostream>

using namespace std;

/**
    *Return the number of players who can make it across the course. 
    
    N: Denotes the number of blocks in the course
    K: Which denotes the maximum jump distance of each player
    S: The course represented as a list of strings

 */
int solve(int N, int K, string S) {
    return 0;
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
