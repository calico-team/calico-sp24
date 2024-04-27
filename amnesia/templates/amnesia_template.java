import java.io.*;

class Main {
    private static String start() {
        /*
        Phase 1: Initialize N.
        
        Return a string of digits denoting the initial persistent value.
        */
        // YOUR CODE HERE
        return null; // change, depending on value
    }


    private static String observe(String N, String color) {
        /*
        Phase 2: Observe each brick.
        
        N: a digit string denoting the persistent value from the previous run
        color: a letter ('B', 'S', or 'G') denoting the color of the current brick
        
        Return a string of digits denoting the updated persistent value for the next
        run. This string must have the same length as the given N.
        */
        // YOUR CODE HERE
        return null; // change, depending on value
    }


    private static String answer(String N) {
        /*
        Phase 3: Submit the final answer.
        
        N: a digit string denoting the persistent value from the previous run
        
        Return a string of length 3 containing each of the characters 'B', 'S', and
        'G' exactly once, denoting the types from least to most frequent. For
        example, if silver was the least frequent, gold was in the middle, and
        bronze was the most frequent, then you should output 'SGB'
        */
        // YOUR CODE HERE
        return null; // change, depending on value
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String phase;
        phase = br.readLine();
        if (phase == "START")
            System.out.println(start());
        else if (phase == "OBSERVE") {
            String N = br.readLine();
            String color = br.readLine();
            System.out.println(observe(N, color));
        }
        else {
            String N = br.readLine();
            System.out.println(answer(N));
        }
    }
}