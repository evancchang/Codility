def solution(H):
    n = len(H)
    if n < 1 or n > 100000:
        return -1

    ans = 0
    stack = []

    for i in xrange(n):
        if H[i] < 1 or H[i] > 1000000000:
            return -1

        #print("*** i = %d ***" %i)
        while stack and H[i] < stack[-1]:
            stack.pop()
            ans += 1

        if stack == [] or H[i] > stack[-1]:
            stack.append(H[i])

        #print("stack = {}".format(stack))
        #print("ans = {}".format(ans))

    return ans + len(stack)

print solution([2,5,1,4,6,7,9,10,1,2])
