import random

COUNTER_SIZE = 2
COUNTERS = 3
COUNT_PROB = 0.35

def start() -> str:
    return '0' * COUNTER_SIZE * COUNTERS


def observe(N: str, color: str) -> int:
    counters = {'B': N[0:3], 'S': N[3:6], 'G': N[6:9]}
    
    counters[color] = str(min(int(counters[color]) + 1, 99))
    while len(counters[color]) < COUNTER_SIZE:
        counters[color] = '0' + counters[color]
    
    return counters['B'] + counters['S'] + counters['G']


def answer(N: str) -> str:
    counters = {'B': int(N[0:3]), 'S': int(N[3:6]), 'G': int(N[6:9])}
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
