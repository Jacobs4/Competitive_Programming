# Suffered a lot of brain damage for this. You need to know Dynamic Programming to solve this to not suffer brain damage T_T
def abbreviation(a, b):
    m, n = len(a), len(b)
    test = [[False]*(m+1) for _ in range(n+1)]
    test[0][0] = True
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 and j != 0:
                test[i][j] = a[j-1].islower() and test[i][j-1]
            elif i !=0 and j !=0 :
                if a[j-1] == b[i-1]:
                    test[i][j] = test[i-1][j-1]
                elif a[j-1].upper() == b[i-1]:
                    test[i][j]=test[i-1][j-1] or test[i][j-1]
                elif not (a[j-1].isupper() and b[i-1].isupper):
                    test[i][j] = test[i][j-1]
    return "YES" if test[n][m] else "NO"
