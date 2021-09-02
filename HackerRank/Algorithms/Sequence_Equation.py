# Damn, had to suffer a bit of brain damage.
def permutationEquation(p):
    ans = [0]*(len(p)+1)
    temp = [0]
    for i in p:
        temp.append(i)
    p = temp
    for i in range(1, len(p)):
        ans[p[p[i]]] = i
    return ans[1:len(p)]
