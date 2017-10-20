def solution(A):
    max_a = max(A)
    if max_a < 0:
        return max_a

    max_end = max_slice = 0   
    for a in A:
        max_end = max(0, max_end+a)
        max_slice = max(max_slice, max_end)
    return max_slice

print solution([5,-7,3,5,-2,4,-1])
print solution([-1,-2,-3,-4,-8,-3])