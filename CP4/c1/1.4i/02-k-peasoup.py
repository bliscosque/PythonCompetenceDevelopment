n=int(input())
rest=[]
plates=[]
f=False
for _ in range(n):
    k=int(input())
    rest.append(input().rstrip())
    plates.append([])
    for _ in range(k):
        plates[-1].append(input().rstrip())
    if not f and "pea soup" in plates[-1] and "pancakes" in plates[-1]:
        print(rest[-1])
        f=True
if not f:
    print("Anywhere is fine I guess")
