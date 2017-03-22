def solution(X, Y, D):
    if X < 1 or X > 1000000000:
        return -1
    if Y < 1 or Y > 1000000000:
        return -1
    if D < 1 or D > 1000000000:
        return -1

    if X > Y:
        return -1

    jmp_number = 0
    jmp_number = (Y-X)//D
    if ((Y-X)%D) != 0:
        jmp_number += 1

    return jmp_number

solution(1, 5, 30)
