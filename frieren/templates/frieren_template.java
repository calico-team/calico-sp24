import java.io.*;

class Solution {
    /**
     * Return the number of times the person saw the Era Meteor Shower if it happens every fifty years.
     * 
     * Y: year the person was born
     * L: the person's lifespan
     * D: year the Demon Kind was slain and an Era Meteor Shower occurred.
     */
    static int solve(int Y, int L, int D) {
        // YOUR CODE HERE
        return -1;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int Y = Integer.parseInt(temp[0]), L = Integer.parseInt(temp[1]), D = Integer.parseInt(temp[2]);
            out.println(solve(Y, L, D));
        }
        out.flush();
    }
}
