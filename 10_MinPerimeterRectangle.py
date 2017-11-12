def solution(N):
    min_perimeter = 999999999

    i = 1
    while (i * i <= N):
        if (N % i == 0):
            min_perimeter = min(min_perimeter, (N / i) + i)
        i += 1

    return (min_perimeter * 2)

print solution(30)