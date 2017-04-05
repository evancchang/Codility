def solution(A):
    N = len(A)
    if N < 3 or N > 100000:
        return -1

    A.sort()
    if A[0] < -1000 or A[-1] > 1000:
        return -1

    # tip: multiply 2 negatives value = positive value
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])

print solution([-3,1,2,-2,5,6])
