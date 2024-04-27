#include <iostream>

using namespace std;

/**
 * Return the number of times the person saw the Era Meteor Shower if it happens every fifty years.
 * 
* B: year the person was born
* L: the person's lifespan
* E: year the Demon King was slain and an Era Meteor Shower occurred.
 */
int solve(int B, int L, int E) {
    int born = ((B - E) % 50 + 50) % 50;
    int death = (born + L) % 50;
    return L / 50 + (death <= born);
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
