def solution(A):
    n = len(A)
    if n > 4000000:
        return 0
    for a in A:
        if a < 0 or a > 200000:
            return 0

    p = q = max_temp = max_profit = 0
    min_temp = 999999
    for i in xrange(n):
        min_temp = min(min_temp, A[i])
        if min_temp == A[i]:
            p = i

        max_temp = max(max_temp, A[i])
        if max_temp == A[i]:
            q = i
        
        #print('min_temp = {}, max_temp = {}'.format(min_temp, max_temp))
        if q < p:
            max_temp = 0
        else:
            profit = max_temp - min_temp
            max_profit = max(max_profit, profit)

    if max_profit > 0:
        return max_profit
    else:
        return 0

print solution([23171,21011,21123,21366,21013,21367])
print solution([3,6,8,4,7,3,1])
print solution([7,8,5,2,3,6,1])
