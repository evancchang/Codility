def solution(A):
    N = len(A)
    if N <= 0 or N > 100000:
        return 0

    A.sort()
    if A[0] < -2147483648 or A[-1] > 2147483747:
        return 0

    for i in xrange(2, N):
        if (A[i - 2] + A [i - 1]) > A[i]:
            return 1

    return 0
