#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

using ll = long long;

/**
 * Return the probability of your Pokemon with H hit points fainting after
 * being hit N times by Population Bomb, which has M different damage rolls R
 * 
 * H: positive integer
 * N: positive integer
 * M: positive integer
 * R: list of N non-negative numbers
 */
int solve(int H, ll N, int M, vector<int> const& R) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int H, M; ll N;
    cin >> H >> N >> M;
    vector<int> R(M);
    for (int j = 0; j < M; ++j)
        cin >> R[j];
    cout << solve(H, N, M, R) << '\n';
    return 0;
}
