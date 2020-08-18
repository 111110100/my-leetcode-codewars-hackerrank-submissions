def birthdayCakeCandles(ar):
    mar = max(ar)
    return sum([x == mar for x in ar])

candles = [4, 1, 2, 4, 4]

print(birthdayCakeCandles(candles))
