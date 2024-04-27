#include <iostream>

using namespace std;

/**
 * Return the number of times the person saw the Era Meteor Shower if it happens every fifty years.
 * 
 * B: years ago the person was born
 * L: the person's lifespan
 * E: years until the next Era Meteor Shower occurrs
 */
int solve(int B, int L, int E) {
    return 0;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int B, L, E;
        cin >> B >> L >> E;
        cout << solve(B, L, E) << '\n';
    }
}
