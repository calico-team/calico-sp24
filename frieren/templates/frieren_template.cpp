#include <iostream>

using namespace std;

/**
 * Return the number of times the person saw the Era Meteor Shower if it happens every fifty years.
 * 
 * Y: year the person was born
 * L: the person's lifespan
 * D: year the Demon King was slain and an Era Meteor Shower occurred.
 */
int solve(int Y, int L, int D) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int Y, L, D;
        cin >> Y >> L >> D;
        cout << solve(Y, L, D) << '\n';
    }
}
