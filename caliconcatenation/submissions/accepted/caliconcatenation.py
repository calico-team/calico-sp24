def solve(A: str):
    """
    Return the CALICOncatenation of A.

    A: a string of representing a single word
    """

    '''
    Greedily search through the first 6 characters of the word to find the 
    first non-matching character.
    '''
    
    calico = "CALICO"
    calico_lower = "calico"
    matching_count = 0
    

    for i in range(7):
        print(A[0:i], calico_lower[6-i:])
        if A[0:i] == calico_lower[6-i:]:
            matching_count = i

    print(matching_count)
            
    return calico + A[matching_count:]

def main():
    T = int(input())
    for _ in range(T):
        A = input()
        print(solve(A))


if __name__ == '__main__':
    main()
