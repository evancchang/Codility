def solution(A):
    N = len(A)
    if N <= 0 or N > 100000:
        return 0

    right = [0] * N
    left = [0] * N

    for i in xrange(N):
        if A[i] < 0 or A[i] > 2147483647:
            return 0

        right[i] = i + A[i]
        left[i] = i - A[i]

    right.sort()
    left.sort()

    result = 0

    #for lower_i in xrange(N):
    #    for upper_i in xrange(lower_i + 1, N):
    #        if left[lower_i] <= upper_i <= right[lower_i]:
    #            result += 1
    #        elif left[upper_i] <= lower_i <= right[upper_i]:
    #            result += 1
    #        elif left[lower_i] <= left[upper_i] <= right[lower_i]:
    #            result += 1
    #        elif left[lower_i] <= right[upper_i] <= right[lower_i]:
    #            result += 1

    #print("right = {}".format(right))
    #print("left = {}".format(left))

    lower_i = 0
    for upper_i in xrange(N):
        #print("*** upper_i = {} ***".format(upper_i))
        while lower_i < N and right[upper_i] >= left[lower_i]:
            lower_i += 1
            #print("lower_i = {}".format(lower_i))

        result += lower_i - upper_i - 1
        #print("result = {}".format(result))
        if result > 10000000:
            return -1

    return result

print solution([1,5,2,1,4,0])
