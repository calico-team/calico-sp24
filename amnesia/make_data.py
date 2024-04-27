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

import collections
import random
from calico_lib import make_sample_test, make_secret_test, make_data

"""
Seed for the random number generator. We need this so randomized tests will
generate the same thing every time. Seeds can be integers or strings.
"""
SEED = 'i forgor 💀' * 1337


class TestCase:
    """
    Represents all the information needed to create the input and output for a
    single test case.
    """

    def __init__(self, max_N_len, bricks, answer):
        self.max_N_len = max_N_len
        self.bricks = bricks
        self.answer = answer


def make_sample_tests():
    """
    Make all sample test files.
    
    To create a pair of sample test files, call make_sample_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_sample_test for more info.
    """
    bricks = ['B'] * 217 + ['S'] * 41 + ['G'] * 133
    random.shuffle(bricks)
    bricks = 'GBS' + ''.join(bricks)
    
    # These claims were made in the pdf sample explanations
    assert bricks.count('B') == 218 and bricks.count('S') == 42 and bricks.count('G') == 134
    assert len(bricks) == 394
    assert bricks[:3] == 'GBS'
    
    make_sample_test([TestCase(9, bricks, 'SGB')], 'main')
    make_sample_test([TestCase(6, bricks, 'SGB')], 'bonus_1')
    make_sample_test([TestCase(4, bricks, 'SGB')], 'bonus_2')


def make_secret_tests():
    """
    Make all secret test files.
    
    To create a pair of sample test files, call make_secret_test with a list of
    TestCase as the first parameter and an optional name for second parameter.
    See calico_lib.make_secret_test for more info.
    """
    def make_grouped_bricks(answer, order, quantities=[50, 125, 225], shuffles=20):
        counts = {answer[i]: quantities[i] for i in range(3)}
        bricks = order.replace('B', 'B' * counts['B']) \
                      .replace('S', 'S' * counts['S']) \
                      .replace('G', 'G' * counts['G'])
        bricks = list(bricks)
        for _ in range(shuffles):
            i, j = random.randrange(0, len(bricks)), random.randrange(0, len(bricks))
            bricks[i], bricks[j] = bricks[j], bricks[i]
        bricks = ''.join(bricks)
        
        return bricks
    
    answers = ['BSG', 'BGS', 'SBG', 'SGB', 'GBS', 'GSB']
    random.shuffle(answers)
    orders = ['BSG', 'BGS', 'SBG', 'SGB', 'GBS', 'GSB']
    random.shuffle(orders)
    quantities = [[random.randint(40, 60), random.randint(115, 135), random.randint(215, 235)] for _ in range(6)]
    
    bricks = [make_grouped_bricks(answers[i], orders[i], quantities[i]) for i in range(6)]
    
    all_tests = {'main': [], 'bonus_1': [], 'bonus_2': []}
    
    for max_N_len, test_set in zip([9, 6, 4], ['main', 'bonus_1', 'bonus_2']):
        for i in range(6):
            all_tests[test_set].append([TestCase(max_N_len, bricks[i], answers[i])])
    
    def rand_answer():
        answer = list('BSG')
        random.shuffle(answer)
        answer = ''.join(answer)
        return answer
    
    def rand_order():
        order = list('BSG')
        random.shuffle(order)
        order = ''.join(order)
        return order
    
    answers = [rand_answer() for _ in range(4)]
    orders = [rand_order() for _ in range(4)]
    quantities = [[40, 135, 215], [40, 135, 215], [60, 115, 215], [60, 115, 215]]
    
    for max_N_len, test_set in zip([9, 6, 4], ['main', 'bonus_1', 'bonus_2']):
        for i in range(4):
            bricks = make_grouped_bricks(answers[i], orders[i], quantities[i], shuffles=1000)
            all_tests[test_set].append([TestCase(max_N_len, bricks, answers[i])])
    
    for test_set in ['main', 'bonus_1', 'bonus_2']:
        for case in all_tests[test_set]:
            make_secret_test(case, test_set)


def make_test_in(cases, file):
    """
    Print the input of each test case into the file in the format specified by
    the input format.
    """
    assert len(cases) == 1
    
    max_N_len, bricks, answer = cases[0].max_N_len, cases[0].bricks, cases[0].answer
    
    assert type(max_N_len) == int
    assert 4 <= max_N_len <= 9
    
    assert type(bricks) == str
    assert set(bricks) == set('BSG')
    a, b, c = sorted(collections.Counter(bricks).items(), key=lambda kv: kv[1])
    assert 40 <= a[1] <= 60
    assert 115 <= b[1] <= 135
    assert 215 <= c[1] <= 235
    
    assert type(answer) == str
    assert len(answer) == 3
    assert set(answer) == set('BSG')
    assert answer == a[0] + b[0] + c[0]
    
    print(max_N_len, file=file)
    print(bricks, file=file)


def make_test_out(cases, file):
    """
    Print the expected output of the test cases into the file in the format
    specified by the output format.
    
    The easiest way to do this is to import a python reference solution to the
    problem and print the output of that.
    """
    assert len(cases) == 1
    
    max_N_len, bricks, answer = cases[0].max_N_len, cases[0].bricks, cases[0].answer
    
    print(answer, file=file)


def main():
    """
    Let the library do the rest of the work!
    """
    make_data(make_sample_tests, make_secret_tests, \
              make_test_in, make_test_out, SEED)


if __name__ == '__main__':
    main()
