def hurdleRace(k, height):
    height.sort(reverse=True)
    if k >= height[0]:
        return 0
    else:
        return height[0]-k
