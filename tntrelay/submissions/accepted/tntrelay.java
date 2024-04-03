import java.io.*;

class Solution {
    /**
     * Return the sum of A and B.
     * 
     * A: a non-negative integer
     * B: another non-negative integer
     */
    static int solve(int A, int B, String C) {
        // YOUR CODE HERE

        /*
        The intuition behind this solution is to use a sliding window
        to find the maximum number of empty spaces in any segment of length B
        */

        int maximum_empty_spaces = 0;
        int temp_empty_spaces = 0;

        if (B >= A) {
            return B;
        }
        
        for (int i = 0; i < A; i++) {
            if (i <= (B - 1)) {
                if (C.charAt(i) == '-') {
                    temp_empty_spaces += 1;
                }
            } else {
                if (C.charAt(i) == '-') {
                    temp_empty_spaces += 1;
                } if (C.charAt(i - B - 1) == '-') {
                    temp_empty_spaces -= 1;
                }
            }
            maximum_empty_spaces = Math.max(maximum_empty_spaces, temp_empty_spaces);
        }
        return Math.max(0, B - maximum_empty_spaces + 1);
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int A = Integer.parseInt(temp[0]), B = Integer.parseInt(temp[1]);
            String[] temp1 = in.readLine().split(" ");
            String C = temp1[0];
            out.println(solve(A, B, C));
        }
        out.flush();
    }
}
