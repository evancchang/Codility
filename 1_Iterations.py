def solution(N):
    if N < 1 or N > 2147483647:
        return -1
    bin_out = bin(N)[2:] #remove 0b
    #print bin_out
    gap_count = 0
    max_gap_count = 0
    num1_count = 0
    for i in bin_out:
        if i == '1':
            num1_count += 1
        if i == '0' and num1_count == 1:
            gap_count += 1
        if num1_count == 2:
            if max_gap_count < gap_count:
                max_gap_count = gap_count
            num1_count = 1
            gap_count = 0
    #print(max_gap_count)
    return max_gap_count

solution(1162)
