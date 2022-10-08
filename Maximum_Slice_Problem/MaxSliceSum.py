def solution(A):
    maxSlice = maxNum = A[0]
    for a in A[1:]:
        maxNum = max(a, maxNum + a)
        maxSlice = max(maxSlice, maxNum)
    return maxSlice
    pass