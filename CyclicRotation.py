from collections import deque
def solution(A, K):
    test_list = deque(A)
    test_list.rotate(K)
    return list(test_list)
    pass