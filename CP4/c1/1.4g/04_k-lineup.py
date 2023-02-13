n=int(input())
a=[]
for _ in range(n):
    a.append(input())
asorted=sorted(a)
arevsorrted=sorted(a,reverse=True)
if a==asorted:
    print("INCREASING")
elif a==arevsorrted:
    print("DECREASING")
else: 
    print("NEITHER")