import java.io.*;
import java.util.HashMap;
import java.util.Map;
import java.util.StringJoiner;

class Solution {
    /**
     * Uses a hashmap which maps characters to their frequencies in both the 
     * player's list and the chest's list. To construct the new list where 
     * duplicate elements are adjacent, iterate over the hashmap's characters
     * and re-add them according to their corresponding frequencies.
     */
    static void solve(int N, int M, char[] P, char[] C) {
        Map<Character, Integer> counts = new HashMap<>();
        
        for (char c : P) {
            int amt = counts.getOrDefault(c, 0);
            counts.put(c, amt + 1);
        }
        for (char c : C) {
            int amt = counts.getOrDefault(c, 0);
            counts.put(c, amt + 1);
        }

        StringJoiner str = new StringJoiner(" ");
        for (char c : counts.keySet()) {
            int amt = counts.get(c);
            for (int i = 0; i < amt; i++) {
                str.add(String.valueOf(c));
            }
        }

        System.out.println(str.toString());
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
