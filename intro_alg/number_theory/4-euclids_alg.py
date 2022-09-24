#calcula GCD (MDC)
def euclid(a,b):
    if (b==0):
        return a
    return euclid(b, a%b)

print(euclid(30,21))
print(euclid(21,30))