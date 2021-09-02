def jumpingOnClouds(c, k):
    e  = 100
    n=len(c)
    i = 0
    j = (i+k)%n
    while True:
        j = (i+k)%n
        if j==0:
            if c[0]==1:
                return e-3
            else:
                return e-1            
        if c[j] == 1:
            e = e-3
        else:
            e-=1
        i=j
