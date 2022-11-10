data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    print(m)
    v = m[0][0]
    print(v)
    for row in m:
        for element in row:
            if v < element: v = element
 
    return v
print(fun(data[0]))