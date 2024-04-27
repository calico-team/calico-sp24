COUNTER_SIZE = 3
COUNTERS = 2

def start() -> str:
    return '0' * COUNTER_SIZE * COUNTERS


def observe(N: str, color: str) -> str:
    counters = {'B': N[0:3], 'S': N[3:6]}
    
    if color != 'G':
        counters[color] = str(int(counters[color]) + 1)
        while len(counters[color]) < COUNTER_SIZE:
            counters[color] = '0' + counters[color]
    
    return counters['B'] + counters['S']


def answer(N: str) -> str:
    counters = {'B': int(N[0:3]), 'S': int(N[3:6])}
    
    if not (40 <= counters['B'] <= 60 or 40 <= counters['S'] <= 60):
        counters['G'] = 50
    elif not (115 <= counters['B'] <= 135 or 115 <= counters['S'] <= 135):
        counters['G'] = 125
    else:
        counters['G'] = 225
    
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
