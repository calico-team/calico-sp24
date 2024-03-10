import java.io.*;

class Solution {
    /**
     * Return the CALICOncatenation of A.
     *
     * A: a string of representing a single word 
     */
    static String solve(String A) {
        String calico = "CALICO";
        String calico_lower = "calico";
        int max_character_match = 0;

        for (int i = 0; i < 7; i++) {
            if (i > A.length()) {
                break;
            }
            String A_substring = A.substring(0, i);
            String calico_substring = calico_lower.substring(6-i);
            if (A_substring.equals(calico_substring)) {
                max_character_match = i;
            }
        }
        return calico + A.substring(max_character_match);
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

