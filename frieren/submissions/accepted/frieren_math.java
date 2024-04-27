import java.io.*;

class Solution {
    static int solve(int B, int L, int E) {
        int age_at_first_shower = (E + B) % 50;
        
        if (age_at_first_shower > L) {
            return 0;
        }
        
        int years_from_first_shower = L - age_at_first_shower;
        return years_from_first_shower / 50 + 1;
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
