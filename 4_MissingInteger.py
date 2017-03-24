def solution(A):
    N = len(A)
    if N < 1 or N > 100000:
        return -1

    A.sort()
    miss_val = 1
    for i in range(N):
        if A[i] < -2147483648 or A[i] > 2147483647:
            return -1

        if A[i] > 0:
            if A[i] == miss_val:
                miss_val += 1

    return miss_val

print solution([1])
