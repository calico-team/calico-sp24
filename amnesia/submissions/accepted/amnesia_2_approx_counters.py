import random

def start() -> str:
    return '0' * 2 * 2


def observe(N: str, color: str) -> str:
    counters = {'B': N[0:2], 'S': N[2:4]}
    
    if color != 'G' and random.random() < 0.6:
        counters[color] = str(min(int(counters[color]) + 1, 99))
        while len(counters[color]) < 2:
            counters[color] = '0' + counters[color]
    
    return counters['B'] + counters['S']


def answer(N: str) -> str:
    counters = {'B': int(N[0:2]), 'S': int(N[2:4])}
    
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
