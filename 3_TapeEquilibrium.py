def solution(A):
    N = len(A)
    if N < 2 or N > 100000:
        return -1

    min_difference = 999999
    total = sum(A)
    inc = 0
    for i in xrange(0, N-1):
        if A[i] < -1000 or A[i] > 1000:
            return -1

        # A = [3,1,2,4,3]
        # p = 1, diff = abs(3-10) = 7
        #             => sum(A) - A[0] - A[0] = 7
        # P = 2, diff = abs(4-9) = 5
        #             => sum(A) - (A[0]+A[1]) - (A[0]+A[1]) = 5

        inc += A[i]
        t = inc*2
        d = abs(total-t)

        if min_difference > d:
            min_difference = d

    return min_difference

solution([1000,-1000])
