def solution(A, B, K):
    if A > B:
        return -1
    if A < 0 or A > 2000000000:
        return -1
    if B < 0 or B > 2000000000:
        return -1
    if K < 1 or K > 2000000000:
        return -1

    if A % K == 0:
        edge = 1
    else:
        edge = 0

    return B//K - A//K + edge


print solution(6, 11, 2)
