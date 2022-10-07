def solution(A):
    newA = list(dict.fromkeys(A))
    return 1 if len(newA) == max(A) == len(A) else 0
    pass