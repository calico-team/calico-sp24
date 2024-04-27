#include <bits/stdc++.h>

using namespace std;

string start() {
    /*
    Phase 1: Initialize N.
    
    Return a string of digits denoting the initial persistent value.
    */
    // YOUR CODE HERE
}


string observe(string N, string color) {
    /*
    Phase 2: Observe each brick.
    
    N: a digit string denoting the persistent value from the previous run
    color: a letter ('B', 'S', or 'G') denoting the color of the current brick
    
    Return a string of digits denoting the updated persistent value for the next
    run. This string must have the same length as the given N.
    */
    // YOUR CODE HERE
}


string answer(string N) {
    /*
    Phase 3: Submit the final answer.
    
    N: a digit string denoting the persistent value from the previous run
    
    Return a string of length 3 containing each of the characters 'B', 'S', and
    'G' exactly once, denoting the types from least to most frequent. For
    example, if silver was the least frequent, gold was in the middle, and
    bronze was the most frequent, then you should output 'SGB'
    */
    // YOUR CODE HERE
}


int main() {
    string phase;
    cin >> phase;
    if (phase == "START")
        cout << start() << endl;
    else if (phase == "OBSERVE") {
        string N, color;
        cin >> N >> color;
        cout << observe(N, color) << endl;
    }
    else {
        string N;
        cin >> N;
        cout << answer(N) << endl;
    }
}
