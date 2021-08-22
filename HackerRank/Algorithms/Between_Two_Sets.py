#I'm not sure, this logic can be simpler but anyway works like a charm
def getTotalX(a, b):
    count = 0
    flag = True
    for i in range(a[len(a)-1], b[0]+1):
        for j in a:
            if i%j != 0:
                flag = False
                break
        if flag:
            for j in b:
                if j%i != 0:
                    flag = False
                    break 
        if flag:
            count += 1
        flag = True    
    return count
