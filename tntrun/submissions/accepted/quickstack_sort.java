import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    /**
     * Combines the player's list with the chest's list and then sorts 
     * the resulting list. Naturally, this makes duplicate elements adjacent 
     * to each other.
     */
    static void solve(int N, int M, char[] P, char[] C) {
        List<String> newChest = new ArrayList<>();

        for (char c : P) {
            newChest.add(String.valueOf(c));
        }
        for (char c : C) {
            newChest.add(String.valueOf(c));
        }

        Collections.sort(newChest);
        System.out.println(String.join(" ", newChest));
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]);
            int M = Integer.parseInt(temp[1]);
            char[] P = new char[N];
            temp = in.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                P[j] = temp[j].charAt(0);
            }
            char[] C = new char[M];
            temp = in.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                C[j] = temp[j].charAt(0);
            }
            solve(N, M, P, C);
        }
        out.flush();
    }
}
