import java.io.*;
import java.util.*;

class Solution {
    /**
     * For each game, output who wins the game in one line.
     *
     * N: size of the game board
     * M: number of different games
     * A: game board
     * G: description of each game
     */
    static List<Integer> primes = null;
    static BitSet bs = null;
    static int SZ;

    static void sieve() {
        primes = new ArrayList<Integer>();
        bs = new BitSet(3200);
        bs.set(0, 3200, true);
        bs.set(0, false);
        bs.set(1, false);
        for (int i = 2; i < 3200; i++) {
            if (bs.get(i)) {
                for (int j = i * i; j < 3200; j += i) bs.set(j, false);
                primes.add(i);
            }
        }
    }

    static Map<Integer, Integer> factorize(int x) {
        Map<Integer, Integer> cnt = new HashMap<Integer, Integer>();
        for (int p : primes) {
            if (p * p > x) break;
            while (x % p == 0) {
                cnt.put(p, cnt.getOrDefault(p, 0 + 1));
                x /= p;
            }
        }
        if (x > 1) cnt.put(x, 1);
        return cnt;
    }

    static int update(int i, int add, int aux, List<Map<Integer, Integer>> factors, Map<Integer, Integer> cnt) {
        for (Map.Entry<Integer, Integer> me : factors.get(i).entrySet()) {
            if (!cnt.containsKey(me.getKey())) cnt.put(me.getKey(), 0);
            aux = aux ^ cnt.get(me.getKey());
            cnt.put(me.getKey(), cnt.get(me.getKey()) + me.getValue() * add);
            aux = aux ^ cnt.get(me.getKey());
        }
        return aux;
    }

    static void solve(int N, int M, int[] A, int[][] G) {
        SZ = (int)(Math.sqrt(N));
        if (primes == null) sieve();
        List<List<Integer>> games = new ArrayList<List<Integer>>(M);
        for (int i = 0; i < M; ++i) {
            games.set(i, new ArrayList<Integer>());
            for (int j = 0; j < 2; ++j) {
                games.get(i).add(G[i][j]);
            }
            games.get(i).add(i);
        }
        List<Map<Integer, Integer>> factors = new ArrayList<Map<Integer, Integer>>(N);
        for (int i = 0; i < N; ++i) {
            factors.set(i, factorize(A[i]));
        }
        games.sort((g1, g2) -> {
            Integer l1 = g1.get(0), l2 = g2.get(0);
            Integer r1 = g1.get(1), r2 = g2.get(0);
            if (l1 / SZ == l2 / SZ) return Integer.compare(r1, r2);
            else return Integer.compare(l1, l2);
        });
        Map<Integer, Integer> cnt = new HashMap<Integer, Integer>();
        List<Boolean> answers = new ArrayList<Boolean>(N);
        int cur_l = 0, cur_r = -1, ans = 0;
        for (List<Integer> q : games) {
            while (cur_l > q.get(0)) {
                cur_l--;
                ans = update(cur_l, 1, ans, factors, cnt);
            }
            while (cur_l < q.get(0)) {
                ans = update(cur_l, -1, ans, factors, cnt);
                cur_l++;
            }
            while (cur_r > q.get(1)) {
                ans = update(cur_r, -1, ans, factors, cnt);
                cur_r--;
            }
            while (cur_r < q.get(1)) {
                cur_r++;
                ans = update(cur_r, 1, ans, factors, cnt);
            }
            answers.set(q.get(2), ans != 0);
        }

        for (int i = 0; i < N; ++i) {
            if (answers.get(i)) {
                out.println("IGNACIO");
            } else {
                out.println("COUSIN");
            }
        }

    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        String[] info = in.readLine().strip().split(" ");
        int N = Integer.parseInt(info[0]);
        int M = Integer.parseInt(info[1]);

        int[] A = new int[N];
        int[][] G = new int[M][2];

        info = in.readLine().strip().split(" ");
        for (int i = 0; i < N; ++i) {
            A[i] = Integer.parseInt(info[i]);
        }
        for (int i = 0; i < M; ++i) {
            info = in.readLine().strip().split(" ");
            for (int j = 0; j < 2; ++j) {
                G[i][j] = Integer.parseInt(info[j]);
            }
        }
        solve(N, M, A, G);
        out.flush();
    }
}
