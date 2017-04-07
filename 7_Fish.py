def solution(A, B):
    if len(A) != len(B):
        return 0

    n = len(A)
    if n < 1 or n > 100000:
        return 0

    if n != len(set(A)):
        return 0

    fish_upstream = []
    fish_downstream = []
    start_eat_fish = False

    # First, save the upstream fish.
    # When the downstream fish appears, check the following upstream fish until the end or be eaten by upstream fish.
    for i in xrange(n):
        if A[i] < 0 or A[i] > 1000000000:
            return 0
        if B[i] not in [0, 1]:
            return 0

        if B[i] == 0:
            if start_eat_fish:
                while fish_downstream:
                    if fish_downstream[-1] < A[i]:
                        fish_downstream.pop()
                    else:
                        break

                if fish_downstream == []:
                    fish_upstream.append(A[i])
            else:
                fish_upstream.append(A[i])
        else:
            start_eat_fish = True
            fish_downstream.append(A[i])

        #print("fish_upstream = {}".format(fish_upstream))
        #print("fish_downstream = {}".format(fish_downstream))
        #print("=====")

    return len(fish_upstream) + len(fish_downstream)

print solution([4,3,2,1,5], [0,1,0,0,0])
