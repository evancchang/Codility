def solution(A):
    n = len(A)
    if n <= 3 or n > 100000:
        return 0

    for a in A:
        if a < -10000 or a > 10000:
            return 0

    max_end = [0] * n
    temp_max_end = 0
    for i in xrange(1, n-1):
        temp_max_end = max(0, temp_max_end+A[i])
        max_end[i] = temp_max_end

    max_begin = [0] * n
    temp_max_begin = 0
    for i in xrange(n-2, 1, -1):
        temp_max_begin = max(0, temp_max_begin+A[i])
        max_begin[i] = temp_max_begin

    max_double_slice = 0
    for i in xrange(0, n-2):
        max_double_slice = max(max_double_slice, max_end[i]+max_begin[i+2])

    return max_double_slice


print solution([3,2,6,-1,4,5,-1,2])
print solution([5,5,5])
print solution([5,17,0,3])
print solution([5,0,1,0,5])




