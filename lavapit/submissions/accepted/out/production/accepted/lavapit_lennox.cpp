#include <bits/stdc++.h>
#define MININT 0x80000000
#define MAXINT 0x7FFFFFFF
#define ent '\n'
#define ff first
#define ss second
#define eb emplace_back
#define sqr(x) ((x)*(x))
#define sz(x) ((int)(x).size())
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef long double ld; 
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ull, ull> pull;

#ifdef LOC
typedef chrono::high_resolution_clock Clock;
#endif

struct state{
	int no, yes; 
	int used, row, col; 
	// no = never used bucket
	// yes = use bucket here
	// used = used bucket but not this row or column
	// row = used bucket somewhere this row
	// col = used bucket somewhere this column
};
const int N = 1005;
int n, m;
state dp[N][N];
string g[N];

inline void printstate(state x){
	cout << "{" << x.no << "," << x.yes << "," << x.used << ',' << x.row << ',' << x.col << "} ";
}

inline void update(int i, int j){
	state down, right;
	memset(&down, 0xFF, sizeof(down));
	memset(&right, 0xFF, sizeof(right));

	if(i != 0){ // go down
		down.yes = dp[i-1][j].no; // Water covered Lava
		down.no = g[i][j]!='L' ? dp[i-1][j].no : -1;
		down.col = max(dp[i-1][j].col, dp[i-1][j].yes);
		down.used = g[i][j]!='L' ? max(dp[i-1][j].row, dp[i-1][j].used) : -1;
	}
	if(j != 0){ // go right
		right.yes = dp[i][j-1].no;
		right.no = g[i][j]!='L' ? dp[i][j-1].no : -1;
		right.row = max(dp[i][j-1].row, dp[i][j-1].yes);
		right.used = g[i][j]!='L' ?  max(dp[i][j-1].col, dp[i][j-1].used) : -1;
	}

	int* dpptr = (int*)(&dp[i][j]);
	int* downptr = (int*)(&down);
	int* rightptr = (int*)(&right);

	for(int k=0; k<5; k++){
		*(dpptr+k) = max(*(downptr+k), *(rightptr+k));
		if(*(dpptr+k)!=-1 && g[i][j]=='D') *(dpptr+k) += 1;
	}
}

void solve(){
	cin >> n >> m;
	for(int i=0; i<n; i++) cin >> g[i];

	memset(dp, 0xFF, sizeof(dp)); //Initialize -1

	if(g[0][0]=='L') dp[0][0].yes = 0; //Only choice, use water here
	if(g[0][0]=='D') dp[0][0].yes = dp[0][0].no = 1;
	if(g[0][0]=='O') dp[0][0].yes = dp[0][0].no = 0;

	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			if(i==0 && j==0) continue;
			update(i, j);
		}
	}
	int ans = MININT;
	for(int i=0; i<5; i++) ans = max(ans, *((int*)(&dp[n-1][m-1]) + i));
//	cout << endl;
//	for(int i=0; i<n; i++){
//		for(int j=0; j<m; j++){
//			printstate(dp[i][j]);
//		}
//		cout << endl;
//	}
//	cout << endl;
	if(ans != -1) cout << ans << ent;
	else cout << "IMPOSSIBLE" << ent;
}

int main(){
	#ifdef LOC
		auto t1 = Clock::now();
	#endif
	ios::sync_with_stdio(0);
	cin.tie(0);

	int tt;
	cin >> tt;
	while(tt--){
		solve();
	}


	#ifdef LOC
		auto t2 = Clock::now();
		auto tmp = chrono::duration_cast<chrono::nanoseconds>(t2-t1);
		ld dur = (ld)tmp.count() * 0.000001;
		cout << "________________________" << endl;
		cout << fixed << setprecision(3) << "finished in " << dur << "ms" << endl;
	#endif
	return 0;
}
