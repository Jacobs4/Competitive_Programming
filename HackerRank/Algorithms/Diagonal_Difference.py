# replace your function with this
def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    n = len(arr)
    for i in range(0, n):
        sum1 += arr[i][i]
    j = n-1
    for i in range(0, n):
        sum2 += arr[i][j]
        j -= 1
            
    return abs(sum1-sum2)
