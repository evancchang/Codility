def solution(A, K):
    if K < 0 or K > 100:
        return []

    N = len(A)
    if N < 0 or N > 100:
        return []

    for i in xrange(0, N):
        if A[i] < -1000 or A[i] > 1000:
            return []
    if N:
        K %= N # because some case K > N
    return A[N-K:] + A[:N-K]

solution([], 0)
