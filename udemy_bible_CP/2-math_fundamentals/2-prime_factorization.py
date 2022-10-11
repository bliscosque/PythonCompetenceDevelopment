from math import sqrt
def primeFact(n):
    print('check: ', n)
    for i in range(2,int(sqrt(n)+1)):
        while n%i==0:
            print(i)
            n/=i
        if n==1:
            return
    print(n) #n é primo

primeFact(10)
primeFact(121)
primeFact(131)
primeFact(500)
