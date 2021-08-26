def countingValleys(steps, path):
    ans = 0
    flag = False
    temp  = 0
    for i in path:
        if i == "D":
            flag = True
            temp -= 1
        else:
            temp += 1
        if flag == True and temp  == 0 and i == "U":
            ans += 1
            flag =False
    return ans
