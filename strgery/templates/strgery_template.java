import java.io.*;

class Solution {
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    /**
     * Print the start positions and lengths of two substrings of S, s1 and s2,
     * such that concatenating s1 and s2 yields to P.
     *
     * S: The string you must find the substrings s1 and s2 in.
     * P: The string you want to make by concatenating.
     *
     * Print your answer instead of returning them.
     */
    static void solve(String S, String P) {
        return;
    }

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String S = in.readLine();
            String P = in.readLine();
            solve(S, P);
        }
        out.flush();
    }
}

