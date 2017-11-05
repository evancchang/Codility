def solution(M, A):
    # write your code in Python 2.7
    n = len(A)
    if n < 1 or n > 100000:
        return -1
    if M < 0 or M > 100000:
        return -1
    for a in A:
        if a < 0 or a > M:
            return -1

    p = 0
    count = 0
    for p in xrange(n):
        print('p = {}'.format(p))
        q = p
        tmp_a = []
        while (q < n):
            if (A[q] not in tmp_a) and (A[q] <= M):
                tmp_a.append(A[q])
                count += 1
                print('p = {}, q = {}'.format(p,q))
                print('tmp_a = {}'.format(tmp_a))
            else:
                break
            q += 1

    return min(count, 1000000000)

def solution2(M, A):
    # write your code in Python 2.7
    n = len(A)
    if n < 1 or n > 100000:
        return -1
    if M < 0 or M > 100000:
        return -1
    for a in A:
        if a < 0 or a > M:
            return -1

    p = count = 0
    has_seen = [0] * (M + 1)
    for q in xrange(n):
        if has_seen[A[q]] != 0:
            while p < q and has_seen[A[q]] != 0:
                has_seen[A[p]] -= 1
                p += 1
        #print('p = {}, q = {}'.format(p, q))
        count += q - p + 1
        has_seen[A[q]] += 1
            
    return min(count, 1000000000)


print solution(6, [3,4,5,5,2])
print('====')
print solution2(6, [3,4,5,5,2])


