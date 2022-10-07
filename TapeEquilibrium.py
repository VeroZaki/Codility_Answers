def solution(A):
    sum_front, sum_back = 0, sum(A)
    diff_list = []
    for elm in A:
        sum_front += elm
        sum_back -= elm
        diff_list.append(abs(sum_front - sum_back))
    diff_list = diff_list[:-1]
    return min(diff_list)