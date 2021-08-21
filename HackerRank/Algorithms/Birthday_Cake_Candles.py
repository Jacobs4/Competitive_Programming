# replace your function with this
def birthdayCakeCandles(candles):
    n = len(candles)
    temp = 0
    count = 0
    for i in candles:
        if i > temp:
            temp = i
            count =  0
        if i == temp:
            count += 1
    return count
