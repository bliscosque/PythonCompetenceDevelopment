def birthdayCakeCandles(candles):
    return candles.count(max(candles))

candles=[4,4,1,3]
print(birthdayCakeCandles(candles))