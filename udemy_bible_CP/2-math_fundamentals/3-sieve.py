maxElem=10000
isPrime = [True]*maxElem

def sieve(n):
    isPrime[0]=isPrime[1]=False
    for i in range(2,(n//2+1)):
        if (isPrime[i]):
            for j in range(i*2,n+1,i):
                isPrime[j]=False

sieve(1000)
for i in range(0,1000):
    if (isPrime[i]): print(i)
