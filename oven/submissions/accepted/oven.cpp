#include <iostream>

using namespace std;

int solve(int D, string A) {
    if (A == "INCREMENT") {
        return D + 1;
    } else if (A == "DECREMENT") {
        return D - 1;
    } else {
        return 0;
    }
}

int main() {
    int D;
    cin >> D;
    string A;
    cin >> A;
    cout << solve(D, A) << '\n';
}
