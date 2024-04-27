#include <iostream>
#include <string>

using namespace std;

string calico = "calico";
string caplico = "CALICO";

string solve(string S) {
    int i = 0;
    int max = 0;
    for (int i = 1; i <= min(6, int(S.size())); ++i) {
        if (calico.substr(6 - i, i) == S.substr(0, i)) {
            max = i;
        }
    }
    if (max == 0) {
        return S;
    } else {
        return caplico + S.substr(max, int(S.size()) - max);
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string S;
        cin >> S;
        cout << solve(S) << '\n';
    }
}
