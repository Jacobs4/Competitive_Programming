def getMoneySpent(keyboards, drives, b):
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)
    temp1 = 0
    ans = []
    for i in keyboards:
        for j in drives:
            if i+j<=b:
                ans.append(i+j)
    if len(ans)==0:       
        return -1
    else:
        ans.sort(reverse=True)
        return ans[0]
