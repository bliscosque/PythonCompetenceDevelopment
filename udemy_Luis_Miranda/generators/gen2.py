def gen():
    yield 1
    print("continua")
    yield 2

g=gen()
print(next(g)) # 1
print(next(g)) # imprime o continua / 2
print(next(g)) # StopIteration
