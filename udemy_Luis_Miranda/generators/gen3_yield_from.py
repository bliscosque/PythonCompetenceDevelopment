def gen1():
    yield 1
    yield 2

def gen2():
    yield from gen1()
    yield 3

g=gen2()
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # 3
print(next(g)) # StopIteration