def strangeCounter(t):
    s=3
    while t>s:
        t-=s
        s*=2
    return s-t+1

print(strangeCounter(11))