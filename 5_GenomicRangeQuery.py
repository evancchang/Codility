def prefix_sums(A):
    n = len(A)
    P = [0] * (n+1)
    for k in xrange(1, n+1):
        P[k] = P[k-1] + A[k-1]

    return P

def solution(S, P, Q):
    N = len(S)
    if N < 1 or N > 100000:
        return []

    if len(P) != len(Q):
        return []
    M = len(P)
    if M < 1 or M > 50000:
        return []

    A = [0] * N
    C = [0] * N
    G = [0] * N
    T = [0] * N

    for i in xrange(N):
        if S[i] == 'A':
            A[i] += 1
        elif S[i] == 'C':
            C[i] += 1
        elif S[i] == 'G':
            G[i] += 1
        elif S[i] == 'T':
            T[i] += 1
        else:
            return []

    pre_A = prefix_sums(A)
    pre_C = prefix_sums(C)
    pre_G = prefix_sums(G)
    pre_T = prefix_sums(T)

    #print("pre_A = {}".format(pre_A))
    #print("pre_C = {}".format(pre_C))
    #print("pre_G = {}".format(pre_G))
    #print("pre_T = {}".format(pre_T))

    ans = [0] * M
    for K in xrange(M):
        if P[K] < 0 or P[K] > N - 1:
            return []
        if Q[K] < 0 or Q[K] > N - 1:
            return []
        if P[K] > Q[K]:
            return []

        hasA = pre_A[Q[K]+1] - pre_A[P[K]]
        hasC = pre_C[Q[K]+1] - pre_C[P[K]]
        hasG = pre_G[Q[K]+1] - pre_G[P[K]]
        hasT = pre_T[Q[K]+1] - pre_T[P[K]]
        # {'A':1, 'C':2, 'G':3, 'T':4}
        if hasA > 0:
            ans[K] = 1
        elif hasC > 0:
            ans[K] = 2
        elif hasG > 0:
            ans[K] = 3
        elif hasT > 0:
            ans[K] = 4
        else:
            pass

    return ans

print solution('CAGCCTA', [2,5,0], [4,5,6]) # return [2,4,1]
