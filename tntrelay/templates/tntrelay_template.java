import java.io.*;

class Solution {
    /**
    * Return the number of players who can make it across the course. 
    
    * N: Denotes the number of blocks in the course
    * K: Which denotes the maximum jump distance of each player
    * S: The course represented as a list of strings
     */
    static int solve(int N, int K, String S) {
        // YOUR CODE HERE
        return -1;
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
