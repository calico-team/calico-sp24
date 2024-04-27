def solve(S: str) -> str:    
    calico = "CALICO"
    calico_lower = "calico"
    matching_count = 0

    for i in range(7):
        if S[0:i] == calico_lower[6 - i:]:
            matching_count = i
            
    return calico + S[matching_count:] if matching_count != 0 else S

def main():
    T = int(input())
    for _ in range(T):
        S = input()
        print(solve(S))


if __name__ == '__main__':
    main()
