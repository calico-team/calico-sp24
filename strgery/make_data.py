#!/usr/bin/env python
"""
Make test data for the problem.

To set up this script, do the following:
    - Set the seed to be something different, long, and arbitrary.
    - Set up the TestCase class to hold relevant information for your problem.
    - Write sample and secret tests in their respective functions.
    - Write input and output code in their respective functions.
Everything else will be handled by the make_data function in calico_lib.py.

You can also run this file with the -v argument to see debug prints.
"""

import random, string
from calico_lib import make_sample_test, make_secret_test, make_data

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'TODO Change this to something different, long, and arbitrary.'


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    
    """

    def __init__(self, A, B):
        self.A = A
        self.B = B


def make_sample_tests():
    """
    Make all sample test files.
    
    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    
    TODO Write sample tests. Consider creating cases that help build
    understanding of the problem, help with debugging, or possibly help
    identify edge cases.
    """
    main_sample_cases = [
            TestCase("calico", "licoca"),
            TestCase("caliconcatenation", "calicocaliconcatenation"),
            TestCase("aaaaaa", "aaaaaaaaaaa"),
            TestCase("caliconcatenation", "tencalico"),
            ]
    make_sample_test(main_sample_cases, 'main')

def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    
    TODO Write sample tests. Consider creating edge cases and large randomized
    tests.

    TODO: more tests...
    - off by one
    - cases where |P| > |S|
    """

    def rand_str(n, c_cnt=26):
        return ''.join(random.choice(string.ascii_lowercase[:c_cnt]) for i in range(n))
    def rand_str_fn(c_cnt):
        return lambda n: rand_str(n, c_cnt)
    def rand_str_2_fn(p1):
        # all 'b' with a small chance of 'a'
        return lambda n: ''.join('a' if random.randint(0, p1) == 0 else 'b' for i in range(n))

    def get_random_substr(s, n):
        """
        Get a random substr of s with length n
        """
        l = len(s)
        assert n <= l

        rng = random.randint(0, 3)
        if rng == 0:
            return s[0:n]
        if rng == 1:
            return s[l-n:]
        pos = random.randint(0, l-n);
        return s[pos:pos+n]

    def generate_cut(s, n): # This generates s2 from 2 cuts of s1, probably correct
        splitPos = random.randint(max(1, n-len(s)), min(n-1, len(s)))
        k = random.randint(splitPos, len(s) - (n-splitPos))
        if random.randint(0, 1) == 0:
            s2 = get_random_substr(s[:k], splitPos) + get_random_substr(s[k:], n-splitPos)
        else:
            s2 = get_random_substr(s[k:], n-splitPos) + get_random_substr(s[:k], splitPos)
        return s2

    def make_random_bad(len1, len2, fn=rand_str):
        s1 = fn(len1)
        s2 = fn(len2)
        return TestCase(s1, s2)
    def make_random_good(len1, len2, fn=rand_str):
        s1 = fn(len1)
        s2 = generate_cut(s1, len2)
        return TestCase(s1, s2)
    def make_swap(len1, len2, fn=rand_str):
        s1 = fn(len1)
        s2 = generate_cut(s1, len2)

        x = random.randint(0, len2-1)
        s2 = s2[:x] + 'a' + s2[x+1:]
        return TestCase(s1, s2)
    def make_random_case(len1, len2, fn=rand_str):
        if len2 > len1 or random.randint(1, 2) == 1:
            return make_random_bad(len1, len2, fn)
        return make_random_good(len1, len2, fn)


    main_edge_cases = [
    ]
    # make_secret_test(main_edge_cases, 'main_edge')

    for i in range(3,6):
        for j in range(3,6):
            for _ in range(10):
                main_random_cases = [make_random_case(i, j, rand_str_fn(5)) for _ in range(10)]
                make_secret_test(main_random_cases, 'main_small')

    for _ in range(10):
        main_random_cases = [make_random_case(random.randint(3,5), random.randint(3,5), rand_str_fn(2)) for _ in range(10)]
        make_secret_test(main_random_cases, 'main_two_char')

    make_secret_test([make_random_case(1000, 1000) for _ in range(5)], "main")
    make_secret_test([make_random_case(1000, 800) for _ in range(5)], "main")
    make_secret_test([make_random_case(1000, 900) for _ in range(5)], "main")
    make_secret_test([make_swap(1000, 800) for _ in range(5)], 'main_one_char_swapped')
    make_secret_test([make_swap(1000, 100) for _ in range(5)], 'main_one_char_swapped')
    make_secret_test([make_swap(1000, 200) for _ in range(5)], 'main_one_char_swapped')

    make_secret_test([make_random_case(i, i, lambda n: 'a'*n) for i in range(2,100)], "main_edge")
    l1 = int(1e5);
    l2 = int(1e5);
    make_secret_test([make_swap(l1, l2) for _ in range(5)], 'bonus_one_char_swapped')
    make_secret_test([make_swap(l1, l2) for _ in range(5)], 'bonus_one_char_swapped')
    make_secret_test([make_swap(l1, l2) for _ in range(5)], 'bonus_one_char_swapped')
    make_secret_test([make_random_case(l1, l1, lambda n: 'a'*n) for i in range(1,2)], "bonus_edge")

    make_secret_test([make_random_case(l1, l2, rand_str_2_fn(4000)) for _ in range(2)], 'bonus_naive_killer')
    make_secret_test([make_random_case(l1, l2, rand_str_2_fn(8000)) for _ in range(2)], 'bonus_naive_killer')
    make_secret_test([make_random_case(l1, l2, rand_str_2_fn(10000)) for _ in range(2)], 'bonus_naive_killer')
    make_secret_test([make_random_case(l1, l2, rand_str_2_fn(40000)) for _ in range(2)], 'bonus_naive_killer')
    make_secret_test([make_random_case(l1, l2, rand_str_2_fn(40000)) for _ in range(2)], 'bonus_naive_killer')
    make_secret_test([make_random_case(l1, l2, rand_str_2_fn(40000)) for _ in range(2)], 'bonus_naive_killer')
    make_secret_test([make_swap(l1, l2, rand_str_2_fn(12000)) for _ in range(2)], 'bonus_naive_killer')
    make_secret_test([make_swap(l1, l2, rand_str_2_fn(12000)) for _ in range(2)], 'bonus_naive_killer')
    make_secret_test([make_swap(l1, l2, rand_str_2_fn(20000)) for _ in range(2)], 'bonus_naive_killer')
    make_secret_test([make_swap(l1, l2, rand_str_2_fn(40000)) for _ in range(2)], 'bonus_naive_killer')
    make_secret_test([make_swap(l1, l2, rand_str_2_fn(40000)) for _ in range(2)], 'bonus_naive_killer')
    make_secret_test([make_swap(l1, l2, rand_str_2_fn(40000)) for _ in range(2)], 'bonus_naive_killer')


def make_test_in(cases: list[TestCase], file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    T = len(cases)
    print(T, file=file)
    for case in cases:
        print(f'{case.A}\n{case.B}', file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    """
    from submissions.accepted.kmp_empty_intersection import solve
    for case in cases:
        print(f"solving {file}: {len(case.A)} {len(case.B)}")
        # try:
        print(solve(case.A, case.B), file=file)
        # except:
            # print("failed on a case :(")
            # print(case.A, case.B)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
