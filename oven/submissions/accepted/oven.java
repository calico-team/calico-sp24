import java.io.*;

class Solution {
    static int solve(int D, String A) {
        if (A.equals("INCREMENT")) {
            return D + 1;
        } else if (A.equals("DECREMENT")) {
            return D - 1;
        } else {
            return D;
        }
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int D = Integer.parseInt(in.readLine());
        String A = in.readLine();
        System.out.println(solve(D, A));
    }
}
