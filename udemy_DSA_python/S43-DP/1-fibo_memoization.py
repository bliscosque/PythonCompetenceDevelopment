def fibMemo(n, memo):
    if n<=2: return n-1
    if not n in memo:
        memo[n]=fibMemo(n-1,memo)+fibMemo(n-2,memo)
    return memo[n]

mydict={}
print(fibMemo(6,mydict))