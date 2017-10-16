# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 2.7
    n = len(A)
    if n < 1 or n > 100000:
        return -1

    for i in A:
        if i < -1000000000 or i > 1000000000:
            return -1

    size = 0
    for k in xrange(n):
        if size == 0:
            size += 1
            value = A[k]
        else:
            if value != A[k]:
                size -= 1
            else:
                size += 1
    
    if size > 0:
        candidate = value
    else:
        return 0

    leader_count = 0
    for k in xrange(n):
        if A[k] == candidate:
            leader_count += 1
    
    if (leader_count <= n//2):
        return 0
    
    count = 0
    left_leader_count = 0
    for i in xrange(n):
        if A[i] == candidate:
            left_leader_count += 1
            leader_count -= 1
        if  (left_leader_count > ((i+1)//2)) and (leader_count > ((n-1-i)//2)):
            count += 1
    return count

print solution([4,3,4,4,4,2])
print solution([1,2,3,4,5,6,7,8])

