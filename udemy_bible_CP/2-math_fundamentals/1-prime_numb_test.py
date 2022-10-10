from math import sqrt

def isPrime(n):
    if n <= 1: return False
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0: return False
    return True

print(isPrime(10))
print(isPrime(131))
print(isPrime(121))
print(isPrime(19))