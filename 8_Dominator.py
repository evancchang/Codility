# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 2.7
    n = len(A)
    if n < 0 or n > 100000:
        return -1

    for i in A:
        if i < -2147483648 or i > 2147483647:
            return -1

    size = 0
    for i in xrange(n):
        if size == 0:
            size += 1
            value = A[i]
        else:
            if value == A[i]:
                size += 1
            else:
                size -= 1
    
    if size > 0:
        candidate = value
    else:
        return -1

    leader_count = 0
    leader_idx = -1
    for i in xrange(n):
        if A[i] == candidate:
            leader_count += 1
            leader_idx = i

    if leader_count > n//2:
        return leader_idx
    else:
        return -1

print solution([3,4,3,2,3,-1,3,3])