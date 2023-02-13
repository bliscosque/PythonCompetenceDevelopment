n=int(input())
a=[int(i) for i in input().split()]
num=sum(i for i in a if i>0)
den=sum(1 for i in a if i>=0)
#print(num,den)
print(num/den)  