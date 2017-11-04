def solution(A):
    # write your code in Python 2.7
    n = len(A)
    if n < 1 or n > 100000:
        return -1

    for a in A:
        if a < -2147483648 or a > 2147483647:
            return -1

    for i in xrange(n):
        if A[i] < 0:
            A[i] = abs(A[i])

    return len(set(A))

print solution([-5,-3,-1,0,3,6])