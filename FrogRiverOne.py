def solution(X, A):
    positions = set() 
    seconds = 0 
 
    for i in range(0, len(A)): 
        if A[i] not in positions and A[i] <= X: 
            positions.add(A[i]) 
            seconds = i 
     
    if len(positions) == X: 
        return seconds

    return -1