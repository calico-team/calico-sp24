#include <iostream>
#include <string>

using namespace std;

string calico = "calico";

string caplico = "CALICO";

string solve(string A) {
    int i = 0;
    int max = 0;
    while (i < min(calico.length(), A.length())) {
        if (calico.substr(calico.length()-i-1 , calico.length()) == A.substr(0, i+1)) {
            max = i;
        }
        i++;
    }
    if (max == 0) {
        return A;
    }
    return caplico + A.substr(max + 1, A.length());
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
