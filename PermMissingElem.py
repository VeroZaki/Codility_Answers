def solution(A):
    length = len(A) + 1
    sumNewList = (length * (length + 1))//2
    return sumNewList - sum(A)
    pass