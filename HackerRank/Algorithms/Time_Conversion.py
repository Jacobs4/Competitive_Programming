def timeConversion(s):
    temp = int(s[0]) * 10
    temp = temp +  int(s[1])
    if s[8] == "P":
        if temp !=  12:
            temp = temp + 12
        temp = str(temp)
    else:
        if temp ==  12:
            temp = 0
            temp =  str(temp) + "0"
        elif temp < 10:
            temp = 0
            temp = str(temp)+ s[1]
        else:
            temp = str(temp)
    ans = temp + s[2:8]
    return ans
