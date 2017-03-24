def solution(X, A):
    N = len(A)
    if N < 1 or N > 100000:
        return -1
    if X < 1 or X > 100000:
        return -1

    s = set()
    for i in xrange(N):
        if A[i] < 1 or A[i] > X:
            return -1

        s.add(A[i])
        if len(s) == X:
            return i

    return -1

print solution(2, [2,2,2,2,2])
