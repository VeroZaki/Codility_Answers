def decimalToBinary(n):
    return bin(n).replace("0b", "")
def solution(N):
    binary = decimalToBinary(N)
    numberCount = []
    res = 0
    count = 0
    for chr in binary:
        if chr == '0':
            count += 1
        else:
            res = max(res, count)
            numberCount.append(res)
            count = 0
    return res
    pass
