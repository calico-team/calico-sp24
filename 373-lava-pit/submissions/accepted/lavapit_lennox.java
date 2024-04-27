import java.util.*;

class lavapit {
    static int inf = 10_000_000;
    static class DpState {
        int no, yes, used, row, col;

        DpState() {
            // Values are -infinity by default and a value < 0 means that you can't reach that state
            no = -inf; // Never used a bucket
            yes = -inf; // Used a bucket in this position
            used = -inf; // Used a bucket but not in this row or column
            row = -inf; // Used a bucket somewhere in this row
            col = -inf; // Used a bucket somewhere in this column
        }
    }

    static String solve(int N, int M, List<String> G) {
        /**
         * Return the maximum number of diamonds that Steve can mine before exiting the lava pit.
         *
         * N: number of rows in the lava pit
         * M: number of columns in the lava pit
         * G: description of the lava pit
         */
        DpState[] memo = new DpState[M];
        for (int j = 0; j < M; j++) {
            memo[j] = new DpState();
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (i != 0 || j != 0) {
                    int[] dp = dpHelper(i, j, G, memo);
                    int no = dp[0], yes = dp[1], used = dp[2], row = dp[3], col = dp[4];

                    int diamond = G.get(i).charAt(j) == 'D' ? 1 : 0;

                    memo[j] = new DpState();
                    memo[j].no = no + diamond;
                    memo[j].yes = yes + diamond;
                    memo[j].used = used + diamond;
                    memo[j].row = row + diamond;
                    memo[j].col = col + diamond;
                }
            }
        }

        int ans = -inf;
        for (DpState state : memo) {
            ans = Math.max(ans, Math.max(Math.max(Math.max(state.no, state.yes), Math.max(state.used, state.row)), state.col));
        }

        if (ans < 0) {
            return "IMPOSSIBLE";
        } else {
            return String.valueOf(ans);
        }
    }

    private static int[] dpHelper(int i, int j, List<String> G, DpState[] memo) {
        int[] no = {-inf}, yes = {-inf}, used = {-inf}, row = {-inf}, col = {-inf};
        if (i != 0) { // Came from (i - 1, j)
            // use bucket at (x, y) = (i, j)
            yes[0] = Math.max(yes[0], memo[j].no);
            // never used bucket
            no[0] = Math.max(no[0], memo[j].no != -inf && G.get(i).charAt(j) != 'L' ? memo[j].no : -inf);
            // used bucket at (x, y) with x < i, y = j
            col[0] = Math.max(col[0], Math.max(memo[j].col, memo[j].yes));
            // used bucket at (x, y) with x < i and y < j
            used[0] = Math.max(used[0], memo[j].row != -inf && memo[j].used != -inf && G.get(i).charAt(j) != 'L' ? Math.max(memo[j].row, memo[j].used) : -inf);
        }

        if (j != 0) { // Came from (i, j - 1)
            // use bucket at (x, y) = (i, j)
            yes[0] = Math.max(yes[0], memo[j - 1].no);
            // never used a bucket
            no[0] = Math.max(no[0], memo[j - 1].no != -inf && G.get(i).charAt(j) != 'L' ? memo[j - 1].no : -inf);
            // used bucket at (x, y) with x < i and y = j
            row[0] = Math.max(row[0], Math.max(memo[j - 1].row, memo[j - 1].yes));
            // used bucket at (x, y) with x < i and y < j
            used[0] = Math.max(used[0], memo[j - 1].col != -inf && memo[j - 1].used != -inf && G.get(i).charAt(j) != 'L' ? Math.max(memo[j - 1].col, memo[j - 1].used) : -inf);
        }

        return new int[]{no[0], yes[0], used[0], row[0], col[0]};
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int x = 0; x < T; x++) {
            int N = scanner.nextInt();
            int M = scanner.nextInt();
            List<String> G = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                G.add(scanner.next());
            }
            System.out.println(solve(N, M, G));
        }
        scanner.close();
    }
}