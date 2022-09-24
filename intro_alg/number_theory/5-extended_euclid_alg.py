#calcula GCD (MDC) e tambem os coeficientes a, b em: mdc(a,b)=ax+by
def extended_euclid(a,b):
    if (b==0):
        return (a,1,0)
    (d1,x1,y1)=extended_euclid(b, a%b)
    (d,x,y)=(d1,y1,x1-(a//b)*y1)
    return (d,x,y)

print(extended_euclid(99,78))