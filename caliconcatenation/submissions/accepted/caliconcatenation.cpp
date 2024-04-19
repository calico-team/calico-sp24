#include <iostream>
#include <string>

using namespace std;

string calico = "calico";

string caplico = "CALICO";

string solve(string A) {
    int i = 0;
    int max = 0;
    for (int i = 1; i <= min(6, int(A.size())); ++i) {
        if (calico.substr(6 - i, i) == A.substr(0, i)) {
            max = i;
        }
    }
    if (max == 0) return A;
    else return caplico + A.substr(max, int(A.size()) - max);
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string A;
        cin >> A;
        cout << solve(A) << '\n';
    }
}
