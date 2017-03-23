def solution(A):
    N = len(A)
    if N < 1 or N > 100000:
        return -1

    count = [0] * (N + 1)
    for val in A:
        if val < 1 or val > 1000000000:
            return -1
        if val > N:
            return 0
        else:
            # if A = [4,1,3,2] then save its count to the count[]
            # count[4] = 1,
            # count[1] = 1 ...
            # => count = [0,1,1,1,1]
            if count[val] > 0:
                return 0
            else:
                count[val] += 1

    #print("count = {}".format(count))
    return 1

print solution([4,1,3,2])
