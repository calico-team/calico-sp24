def solve(A: int, B: int, C: str) -> int:
    """
    Return the sum of A and B.
    
    A: a non-negative integer
    B: A non-empty string
    """
    # YOUR CODE HERE

    '''
    The intuition behind this solution is to use a sliding window
    to find the maximum number of empty spaces in any segment of length B
    '''

    maximum_empty_spaces = 0
    temp_empty_spaces = 0

    if B >= A:
        return -1

    for i in range(A):
        if i <= B-1:
            if C[i] == '-':
                temp_empty_spaces += 1
        else:
            if C[i] == '-':
                temp_empty_spaces += 1
            if C[i-B-1] == '-':
                temp_empty_spaces -= 1
        maximum_empty_spaces = max(maximum_empty_spaces, temp_empty_spaces)

    return max(0, B-maximum_empty_spaces+1)


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        A, B = int(temp[0]), int(temp[1])
        C = input()
        print(solve(A, B, C))

if __name__ == '__main__':
    main()
