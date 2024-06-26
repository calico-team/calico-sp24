import java.io.*;

class Solution {
    static int solve(int N, int K, String S) {
        if (K >= N) {
            return -1;
        }
        ++K;
        int mx = 0, cur = 0;
        for (int i = 0; i < K; ++i) {
            if (S.charAt(i) == '-') {
                ++cur;
            }
            mx = Math.max(cur, mx);
        }
        for (int i = K; i < N; ++i) {
            if (S.charAt(i) == '-') {
                ++cur;
            }
            if (S.charAt(i - K) == '-') {
                --cur;
            }
            mx = Math.max(cur, mx);
        }
        return K - mx;
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]), K = Integer.parseInt(temp[1]);
            String[] temp1 = in.readLine().split(" ");
            String S = temp1[0];
            out.println(solve(N, K, S));
        }
        out.flush();
    }
}
