def solution(A):
    N = len(A)
    if N <= 0 or N > 100000:
        return 0

    A.sort()
    #print("A = {}".format(A))
    result = 1
    for i in xrange(1, N):
        if A[i] < -1000000 or A[i] > 1000000:
            return -1

        if A[i - 1] != A[i]:
            result += 1

    return result

print solution([])
