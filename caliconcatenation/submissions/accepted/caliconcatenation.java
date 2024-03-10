import java.io.*;

class Solution {
    /**
     * Return the CALICOncatenation of A.
     *
     * A: a string of representing a single word 
     */
    static int solve(String A) {
        System.out.println(A);
        return -1;
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String A = in.readLine();
            out.println(solve(A));
        }
        out.flush();
    }
}

