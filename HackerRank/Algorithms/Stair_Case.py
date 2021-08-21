def staircase(n):
    space = n-1
    while space >= 0:
        for i in range(0, space):
            print(" ", end = '')
        for i in range(0, n-space):
            print("#", end='')
        print()
        space -= 1
    return
