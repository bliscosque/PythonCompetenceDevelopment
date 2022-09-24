def power(x,y,p):
    res=1
    while(y>0):
        if ((y&1)!=0): #y é impar, multiplica x pelo resultado
            res*=x%p
        y=y>>1 #y=y//2
        x=(x*x)%p #x=x^2
    return res%p

print(power(2,5,13))