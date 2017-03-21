def solution(A):
    length = len(A)
    if length < 1 or length > 1000000:
        return -1

    for i in xrange(0, length):
        if A[i] < 1 or A[i] > 1000000000:
            return -1
    # XOR operations: X^X=0, and 0^X=X.
    # X ^ (Y ^ Z) = (X ^ Y) ^ Z.
    result = 0
    for number in A:
        result ^= number
    #print result
    return result

solution([42])
