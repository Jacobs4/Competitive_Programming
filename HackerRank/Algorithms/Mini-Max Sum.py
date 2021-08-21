# replace your function with this
def miniMaxSum(arr):
    arr.sort()
    temp = 0
    for i in range(0, len(arr)-1):
        temp += arr[i]
    print(temp, end=' ')
    temp = 0
    for i in range(1, len(arr)):
        temp += arr[i]
    print(temp)
    return
