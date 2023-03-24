def pageCount(n, p):
    from_start=p//2
    if n%2==1:
        from_end=(n-p)//2
    else:
        from_end=(n-p+1)//2
    return min(from_start,from_end)

print(pageCount(5,3))
print(pageCount(6,2))
print(pageCount(5,4))
print(pageCount(6,5)) # 1