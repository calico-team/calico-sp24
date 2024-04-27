import java.io.*;

class Solution {
    /**
     * Return the number of times the person saw the Era Meteor Shower if it happens every fifty years.
     * 
     * Y: year the person was born
     * L: the person's lifespan
     * D: year the Demon King was slain and an Era Meteor Shower occurred.
     */
    static int solve(int B, int L, int E) {
        int born = ((B - E) % 50 + 50) % 50;
        int death = (born + L) % 50;
        if (death <= born) {
            return (L / 50) + 1;
        }
        return (L / 50);
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int B = Integer.parseInt(temp[0]), L = Integer.parseInt(temp[1]), E = Integer.parseInt(temp[2]);
            out.println(solve(B, L, E));
        }
        out.flush();
    }
}
