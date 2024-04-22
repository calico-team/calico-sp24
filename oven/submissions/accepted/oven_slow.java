import java.util.Scanner;

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
    
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int D = sc.nextInt();
        String A = sc.next();
        System.out.println(solve(D, A));
    }
}
