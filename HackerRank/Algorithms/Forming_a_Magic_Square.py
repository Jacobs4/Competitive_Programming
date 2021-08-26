# Damn, I had to suffer brain damage for this one
# wondering what those real 1-8 lists are ? XD. Refer : https://mindyourdecisions.com/blog/2015/11/08/how-many-3x3-magic-squares-are-there-sunday-puzzle/
def formingMagicSquare(s):
    ans = 0
    real1 = [2, 7, 6, 9, 5, 1, 4, 3, 8]
    real2 = [4, 9, 2, 3, 5, 7, 8, 1, 6]
    real3 = [8, 3, 4, 1, 5, 9, 6, 7, 2]
    real4 = [6, 1, 8, 7, 5, 3, 2, 9, 4]
    real5 = [2, 9, 4, 7, 5, 3, 6, 1, 8]
    real6 = [8, 1, 6, 3, 5, 7, 4, 9, 2]
    real7 = [4, 3, 8, 9, 5, 1, 2, 7, 6]
    real8 = [6, 7, 2, 1, 5, 9, 8, 3, 4]
    mini = [0]*8
    copy = []
    for i in range(3):
        for j in s[i]:
            copy.append(j)
    for i in range(0,9):
        mini[0] += abs(real1[i]-copy[i])
        mini[1] += abs(real2[i]-copy[i])
        mini[2] += abs(real3[i]-copy[i])
        mini[3] += abs(real4[i]-copy[i])
        mini[4] += abs(real5[i]-copy[i])
        mini[5] += abs(real6[i]-copy[i])
        mini[6] += abs(real7[i]-copy[i])
        mini[7] += abs(real8[i]-copy[i])
    return min(mini)
