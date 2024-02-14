import java.io.*;

class Solution {
    /**
     * Combines all items from the player and chest into one array,
     * and creates a new array to represent our new chest. For each
     * item, check if we've already added it into our new chest--if
     * so, skip the item. Otherwise, add it and any others like it
     * into the chest.
     */
    static void solve(int N, int M, char[] P, char[] C) {
        // Combining all items into one list
        char[] allItems = new char[N + M];
        for (int i = 0; i < N; i++) {
            allItems[i] = P[i];
        }
        for (int i = 0; i < M; i++) {
            allItems[N + i] = C[i];
        }

        char[] newChest = new char[N + M];
        int itemsInChest = 0;
        for (int i = 0; i < allItems.length; i++) {
            char curItem = allItems[i];

            // Checking if we've already added this item before
            boolean alreadyAdded = false;
            for (int j = 0; j < itemsInChest; j++) {
                if (newChest[j] == curItem) {
                    alreadyAdded = true;
                    break;
                }
            }

            if (alreadyAdded) {
                continue;
            }

            // Finding all items like curItem and adding them
            newChest[itemsInChest] = curItem;
            itemsInChest++;
            for (int j = i + 1; j < allItems.length; j++) {
                if (allItems[j] == curItem) {
                    newChest[itemsInChest] = curItem;
                    itemsInChest++;
                }
            }
        }

        for (int i = 0; i < newChest.length; i++) {
            System.out.print(newChest[i]);
            // We don't punish you for trailing spaces, but it's bad practice to leave them in!
            System.out.print(" ");
        }
        System.out.println("");
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
