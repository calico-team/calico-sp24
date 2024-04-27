#pragma once
#include <bits/stdc++.h>
using namespace std;

struct TestCase {
    /**
     * Represents all information needed to create the input and output for
     * a single test case.
     * 
     * @todo Change this to store the relevant information for your problem.
     * 
    */

    int H;
    long long N;
    int M;
    vector<int> R;
    
    TestCase(int _H, long long _N, int _M, vector<int> _R) : H(_H), N(_N), M(_M), R(_R) {}
    
};

/**
 * @return true if the single test case satisfies the constraints for the
 * main test cases.
 * 
 * @todo change this with the constraints needed for your problem.
 * 
*/
const int MAXH = 1E4;
const long long MAXN = 1E18;
const int MAXM = 2E5;
const int MAXR = 2E4;
bool is_correct_main_case(TestCase const& tc) {
    if (tc.H <= 0 || tc.H > MAXH) return false;
    if (tc.N <= 0 || tc.N > MAXN) return false;
    if (tc.M <= 0 || tc.M > MAXM) return false;
    for (int r : tc.R)
        if (r < 0 || r > MAXR)
            return false;
    return true;
}

/**
 * @return true if the test case batch satisfies the constraints for the
 * main test cases.
 * 
 * @todo change this with the constraints needed for your problem.
 * 
*/
bool is_correct_main_batch(vector<TestCase> const& batch) {
    for (auto& tc : batch)
        if (!is_correct_main_case(tc))
            return false;
    return batch.size() == 1;
}

/**
 * @return true if the single test case satisfies the constraints for the
 * bonus test cases.
 * 
 * @todo change this with the constraints needed for your problem.
 * 
*/
bool is_correct_bonus_case(TestCase const& tc) {
    return true;
}

/**
 * @return true if the test case batch satisfies the constraints for the
 * bonus test cases.
 * 
 * @todo change this with the constraints needed for your problem.
 * 
*/
bool is_correct_bonus_batch(vector<TestCase> const& batch) {
    for (auto& tc : batch)
        if (!is_correct_bonus_case(tc))
            return false;
    return true;
}

/**
 * @todo Implement this operator so that it prints the test case with
 * the correct input format.
*/
inline ostream& operator << (ostream& o, TestCase const& tc) {
    o << tc.H << ' ' << tc.N << ' ' << tc.M << '\n';
    for (int i = 0; i < tc.M; ++i) {
        if (i) o << ' ';
        o << tc.R[i];
    }
    return o;
}