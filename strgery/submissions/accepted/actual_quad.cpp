#include <bits/stdc++.h>
using namespace std;

// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,popcnt,lzcnt")

using vi = vector<int>;

void fastIO() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
}

vi zf(string s) {
	int n = s.size();
	vi z(n);
	int x = 0, y = 0;

	for (int i = 1; i < n; i++) {
		z[i] = max(0, min(z[i - x], y - i + 1));
		while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
			x = i;
			y = i + z[i];
			z[i]++;
		}
	}

	return z;
}

void solve(int i_, int t_) {
	string s, p;
	cin >> s >> p;

	int n = s.size(), m = p.size();
	vi z = zf(p + "$" + s);

	for (int s1 = 0; s1 < n; s1++) {
		int l1 = min(z[m + 1 + s1], m - 1); // Greedily maximize l1
		if (l1 < 1) continue;
		string suf = p.substr(l1); // Substring 2 must cover the rest of p
		int l2 = suf.size();
		// s' is a "censored" version of s that bans overlaps
		string sp = s;
		for (int i = s1; i < s1 + l1; i++) sp[i] = '#';
		// Try to find substring 2 within the remainder of s
		vi z2 = zf(suf + "$" + sp);
		for (int s2 = 0; s2 < n; s2++) {
			if (z2[l2 + 1 + s2] != l2) continue;
			cout << s1 << ' ' << l1 << ' ' << s2 << ' ' << l2 << '\n';
			return;
		}
	}

	cout << "IMPOSSIBLE\n";
}

int main() {
	fastIO();
	int t = 1;
	cin >> t;
	for (int i = 1; i <= t; i++) solve(i, t);
}
