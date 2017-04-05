def prefix_sums(A):
    n = len(A)
    P = [0] * (n+1)
    for k in xrange(1, n+1):
        P[k] = P[k-1] + A[k-1]

    return P

def solution(A):
    N = len(A)
    if N < 2 or N > 100000:
        return -1

    P = prefix_sums(A)

    min_average = 99999
    smallest_start_pos = -1
    #print("P = {}".format(P))

    for i in xrange(N):
        #print("i = %d" %i)
        if A[i] < -10000 or A[i] > 10000:
            return -1

        # The trick to this problem is that the min average slice also cannot be longer than 3.
        # So we only have to calculate the avg of the slices of length 2 and 3.
        if (i + 2) <= N:
            average_2 = (P[i+2] - P[i]) / 2.0
            #print("average_2 = {}".format(average_2))
            if min_average > average_2:
                min_average = average_2
                smallest_start_pos = i

        if (i + 3) <= N:
            average_3 = (P[i+3] - P[i]) / 3.0
            #print("average_3 = {}".format(average_3))
            if min_average > average_3:
                min_average = average_3
                smallest_start_pos = i

    return smallest_start_pos

print solution([1001, -1001])
