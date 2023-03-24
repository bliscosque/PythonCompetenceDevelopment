def fibonacciModified(t1, t2, n):
    m=[t1,t2]
    for i in range(n-2):
        m.append(m[i]+m[i+1]**2)
    #print(m)
    return m[n-1]

print(fibonacciModified(0,1,6))
print(fibonacciModified(0,1,5))