#include <bits/stdc++.h>
#include "calico_lib.cpp"
#include "test_case.cpp"
#include "solution.cpp"
using namespace std;

#define NUMBER_OF_TEST_CASES 1
#define UNLIMITED_TEST_CASES 2 // Use this for problems with just one test case too.
#define SENTINEL_CASE 3

// Change this accordingly to the type of problem.
const int _TYPE_OF_OUTPUT_ = UNLIMITED_TEST_CASES;
// Change this to the sentinel that you want to use in case of the third type of input.
const string SENTINEL = "";
// Change the seed to the number you want.
long long SEED = 33;
mt19937_64 rng;

/**
 * Make all sample test files.
 * 
 * To create a batch of sample test files, call make_samepl_test with a vector of
 * TestCase as the first parameter and an optional name for second parameter.
 * See calico_lib.make_sample_test for more info.
 * 
 * @todo Write sample tests. Consider creating cases that help build
 * understanding of the problem, help with debugging, or possibly help
 * identify edge cases.
 * 
*/
void make_sample_tests() {
    vector<TestCase> main_sample_cases = { TestCase(20, 2, 3, {10, 11, 11}) };
    assert(is_correct_main_batch(main_sample_cases));
    make_sample_test(main_sample_cases, "main_sample");
    
    main_sample_cases = { TestCase(20, 2, 5, {9, 8, 7, 4, 0}) };
    assert(is_correct_main_batch(main_sample_cases));
    make_sample_test(main_sample_cases, "main_sample");

    main_sample_cases = { TestCase(20, 2, 2, {10, 0}) };
    assert(is_correct_main_batch(main_sample_cases));
    make_sample_test(main_sample_cases, "main_sample");
    
    main_sample_cases = { TestCase(1729, 1000, 10, {0, 0, 0, 1, 1, 1, 2, 2, 3, 4}) };
    assert(is_correct_main_batch(main_sample_cases));
    make_sample_test(main_sample_cases, "main_sample");

    // vector<TestCase> bonus_sample_cases = {};
    // assert(is_correct_bonus_batch(bonus_sample_cases));
    // make_sample_test(bonus_sample_cases, "bonus_sample");
}

ll random_range(ll A, ll B) {
    assert(A <= B);
    return A + rng() % (B - A + 1);
}

TestCase random_test_case(int H, ll N, int M) {
    if (H == -1) H = random_range(MAXH / 10 * 9, MAXH);
    if (N == -1) N = random_range(MAXN / 10 * 9, MAXN);
    if (M == -1) M = random_range(MAXM / 10 * 9, MAXM);
    vector<int> R(M);
    for (int i = 0; i < M; ++i)
        R[i] = random_range(0, MAXR);
    int numzeros = random_range(0, M / 10); // This is so its not trivially 1
    for (int i = 0; i < numzeros; ++i)
        R[i] = 0;
    R.back() = random_range(H, MAXR); // This is so its not trivially 0
    return TestCase(H, N, M, R);
}

/**
 * Make all secret test files.
 * 
 * To create a batch of secret test files, call make_secret_test with a list of
 * TestCase as the first parameter and an optional name for second parameter.
 * See calico_lib.make_secret_test for more info.
 * 
 * @todo Write secret tests. Consider creating edge cases and large randomized
 * test cases.
*/
void make_secret_tests() {

    // Generate random test cases for main.
    debug_print("Generating random main");
    for (int i = 0; i < 30; ++i) {
        vector<TestCase> main_random_cases = { random_test_case(-1, -1, -1) };
        assert(is_correct_main_batch(main_random_cases));
        make_secret_test(main_random_cases, "main_random");
    } 
    
    // Generate edge cases for main.
    debug_print("Edging main cases");
    for (int i = 0; i < 5; ++i) {
        vector<TestCase> main_edge_cases =  { random_test_case(MAXH, MAXN, MAXM)};
        assert(is_correct_main_batch(main_edge_cases));
        make_secret_test(main_edge_cases, "main_edge");
    }

    // // Generate random test cases for bonus.
    // debug_print("Generating random bonus");
    // vector<TestCase> bonus_random_cases = {};
    // assert(is_correct_bonus_batch(bonus_random_cases));
    // make_secret_test(bonus_random_cases, "bonus_random");
    
    // // Generate edge cases for bonus.
    // debug_print("Edging bonus cases");
    // vector<TestCase> bonus_edge_cases = {};
    // assert(is_correct_bonus_batch(bonus_edge_cases));
    // make_secret_test(bonus_edge_cases, "bonus_edge");

}

void make_test_in(vector<TestCase>& cases, string const& path) {
    // Leave this as it is. Do not touch it with your dirty hands...
    freopen(path.c_str(), "w", stdout);
    if (_TYPE_OF_OUTPUT_ == NUMBER_OF_TEST_CASES) {
        cout << int(cases.size()) << '\n';
    }
    for (auto& tc : cases) cout << tc << '\n';
    if (_TYPE_OF_OUTPUT_ == SENTINEL_CASE) {
        cout << SENTINEL << '\n';
    }
}

void make_test_out(vector<TestCase>& cases, string const& path) {
    freopen(path.c_str(), "w", stdout);
    for (TestCase& tc : cases)
        solve_and_print(tc);
}

int main() {
    make_data(make_sample_tests, make_secret_tests, make_test_in, make_test_out, SEED, rng);
}