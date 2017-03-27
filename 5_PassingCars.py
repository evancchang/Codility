def solution(A):
    N = len(A)
    if N < 1 or N > 100000:
        return -1

    west = 0
    passing = 0

    for i in xrange(N):
        if A[i] < 0 or A[i] > 1:
            return -1

        if A[i] == 0:
            west += 1
        else:
            passing += west
            if passing > 1000000000:
                return -1

        #print("west = {}".format(west))
        #print("passing = {}".format(passing))
        #print("=======")

    return passing

print solution([0,1,0,1,1])
# [0,1,0,1,1]
#    ------> passing car
#      ----> passing car
