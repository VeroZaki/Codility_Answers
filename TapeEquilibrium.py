# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    maxNum = max(A)
    sum1 = sum(A[:A.index(maxNum)])
    sum2 = sum(A[A.index(maxNum):])
    sum3 = sum(A[:A.index(maxNum)+1])
    sum4 = sum(A[A.index(maxNum)+1:])
    diff1 = abs(sum1 - sum2)
    diff2 = abs(sum3 - sum4)
    return diff1 if diff1 < diff2 else diff2
    pass
