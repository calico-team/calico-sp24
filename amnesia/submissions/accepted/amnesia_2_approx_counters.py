import random

COUNTER_SIZE = 2
COUNTERS = 2
COUNT_PROB = 0.6

def start() -> str:
    return '0' * COUNTER_SIZE * COUNTERS


def observe(N: str, color: str) -> int:
    counters = {'B': N[0:3], 'S': N[3:6]}
    
    if color != 'G' and random.random() < COUNT_PROB:
        counters[color] = str(min(int(counters[color]) + 1, 99))
        while len(counters[color]) < COUNTER_SIZE:
            counters[color] = '0' + counters[color]
    
    return counters['B'] + counters['S']


def answer(N: str) -> str:
    counters = {'B': int(N[0:3]), 'S': int(N[3:6])}
    
    if not (counters['B'] < 50 or counters['S'] < 50):
        counters['G'] = 25
    elif not (50 <= counters['B'] <= 98 or 50 <= counters['S'] <= 98):
        counters['G'] = 75
    else:
        counters['G'] = 99
    
    return ''.join(sorted(counters, key=counters.get))


def main():
    phase = input()
    if phase == 'START':
        print(start())
    elif phase == 'OBSERVE':
        N = input()
        color = input()
        print(observe(N, color))
    else:
        N = input()
        print(answer(N))


if __name__ == '__main__':
    main()
