def solution(A):
    # write your code in Python 2.7
    n = len(A)
    if n < 0 or n > 1000:
        return -1
    for a in A:
        if a < 1 or a > 1000000000:
            return -1

    result = 0
    A.sort()
    #print('A = {}'.format(A))
    for first in xrange(n):
        third = first + 2
        for second in xrange(first + 1, n):
            while (third < n and A[first] + A[second] > A[third]):
                #print('({},{},{})'.format(A[first], A[second], A[third]))
                #print('third = {}, second = {}'.format(third, second))
                third += 1
            result += third - second - 1

    return result

print solution([10,2,5,1,8,12])

