def solution(N, A):
    # write your code in Python 2.7
    if N < 1 or N > 100000:
        return []

    M = len(A)
    if M < 1 or M > 100000:
        return []

    if min(A) < 1 or max(A) > N + 1:
        return []

    max_val = 0
    need_update_val = 0
    count_list = [0] * N
    for val in A:
        if 1 <= val <= N:
            if count_list[val-1] < need_update_val: # when "N +1" trigger, set to the max count then add the count
                count_list[val-1] = need_update_val
            count_list[val-1] += 1
            max_val = max(max_val, count_list[val-1])
        elif val == N + 1:
            need_update_val = max_val
    
    # add max count to those still '0' count
    for i in xrange(N):
        count_list[i] = max(count_list[i], need_update_val)

    return count_list

print solution(5, [3,4,4,6,1,4,4])
