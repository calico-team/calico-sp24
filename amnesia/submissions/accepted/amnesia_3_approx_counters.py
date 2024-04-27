import random

def start() -> str:
    return '0' * 2 * 3


def observe(N: str, color: str) -> str:
    counters = {'B': N[0:2], 'S': N[2:4], 'G': N[4:6]}
    
    if random.random() < 0.35:
        counters[color] = str(min(int(counters[color]) + 1, 99))
        while len(counters[color]) < 2:
            counters[color] = '0' + counters[color]
    
    return counters['B'] + counters['S'] + counters['G']


def answer(N: str) -> str:
    counters = {'B': int(N[0:2]), 'S': int(N[2:4]), 'G': int(N[4:6])}
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
