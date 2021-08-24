def migratoryBirds(arr):
    ans = [0]*6
    for i in arr:
        ans[i] += 1
    temp = max(ans)
    for i in range(len(ans)):
        if ans[i] == temp:
            return i
