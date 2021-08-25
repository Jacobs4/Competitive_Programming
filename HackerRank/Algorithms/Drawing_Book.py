def pageCount(n, p):
    if n%2==0:
        pages =  n//2
    else:
        pages = (n-1)//2
    if p%2==1:
        p -= 1
    ans = p//2
    if ans>pages//2:
        return pages - ans
    else:
        return ans
