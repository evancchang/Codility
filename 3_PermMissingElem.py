def solution(A):
    if not A: # if A = []
        return 1
    N = len(A)
    if N < 0 or N > 100001:
        return -1

    A.sort()

    ans = -1
    for i in xrange(0, N-1):
        if A[i] < 1 or A[i] > N + 1:
            return -1
        elif A[i+1] - A[i] == 0: # duplicate
            return -1
        elif A[i+1] - A[i] > 1:
            ans = A[i+1] - 1

    if ans == -1:
        if A[0] != 1:
            ans = 1
        elif A[N-1] != N + 1:
            ans = N + 1
    return ans
solution([])
