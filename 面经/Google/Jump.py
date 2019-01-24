def solution(A):
    N = len(A)
    odds = [False] * N
    evens = [False] * N
    odds[-1] = True
    evens[-1] = True
    trails = [A[-1]]
    
    for i in reversed(range(N-1)):
        # calculate odd jumps
        diff = 2**32
        for index, value in enumerate(trails):
            # key has to be larger than A[i]
            if value > A[i]:
                if value - A[i] <= diff:
                    odds[i] = evens[N-1-index]
                    diff = value - A[i]
        
        # calculate even jumps
        diff = 2**32
        for index, value in enumerate(trails):
            # has to be smaller than A[i]
            if value < A[i]:
                if A[i] - value <= diff:
                    evens[i] = odds[N-1-index]
                    diff = A[i] - value
        trails.append(A[i])
        
    print(odds, evens)

solution([1,2, 2,3,4,3,2])