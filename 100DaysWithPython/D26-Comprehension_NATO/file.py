with open("file1.txt") as f1:
    nf1=[int(n) for n in f1.readlines()]
print(nf1)
with open("file2.txt") as f2:
    nf2=[int(n) for n in f2.readlines()]
print(nf2)
result=[n for n in nf1 if n in nf2]
print(result)