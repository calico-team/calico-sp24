#include <iostream>
#include <vector>

using namespace std;

/**
 * Output a possible configuration of the chest after performing quickstack
 * 
 * N: the number of items the player has
 * M: the number of items the chest has
 * P: the list of items on the player
 * C: the list of items in the chest
 */
void solve(int N, int M, vector<char> P, vector<char> C) {
    // YOUR CODE HERE
    return;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, M;
        cin >> N >> M;
        vector<char> P(N);
        for (char &item : P) {
            cin >> item;
        }
        vector<char> C(M);
        for (char &item : C) {
            cin >> item;
        }
        solve(N, M, P, C);
    }
}
