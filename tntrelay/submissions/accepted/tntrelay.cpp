#include <iostream>

using namespace std;

/**
 * Implements addition with CPP's fixed precision int. This passes the main test
 * set only.
 */
int solve(int A, int B, string C) {
    int maximum_empty_spaces = 0;
    int temp_empty_spaces = 0;

    if (B > A) {
        return B;
    }
    for(int i = 0; i < A; i++) {
        if (i < B) {
            if (C[i] == '-') {
                temp_empty_spaces++;
            }
        } else {
            if (C[i] == '-') {
                temp_empty_spaces++;
            }
            if (C[i - B] == '-') {
                temp_empty_spaces--;
            }
            maximum_empty_spaces = max(maximum_empty_spaces, temp_empty_spaces);
        }
    }
    return B - maximum_empty_spaces;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int A, B;
        cin >> A >> B;
        string C;
        cin >> C;
        cout << solve(A, B, C) << '\n';
    }
}
