#include <iostream>

using namespace std;

int solve(int B, int L, int E) {
    int age_at_first_shower = (E + B) % 50;
    
    if (age_at_first_shower > L) {
        return 0;
    }
    
    int years_from_first_shower = L - age_at_first_shower;
    return years_from_first_shower / 50 + 1;
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
