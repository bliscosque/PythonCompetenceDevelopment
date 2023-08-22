gen=(n for n in range(2))
print(gen) # <generator object <genexpr> at 0x000001E4CD5E8380>
print (next(gen)) # 0
print (next(gen)) # 1
print (next(gen)) # StopIteration