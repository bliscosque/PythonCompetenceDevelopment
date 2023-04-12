def appendAndDelete(s, t, k):
    def appendAndDelete_int(s, t, k,dct={}):
        if (s,t,k) in dct: return dct[(s,t,k)]
        if k==-1:
            dct[(s,t,k)]='No' 
            return dct[(s,t,k)]
        if s==t and k%2==0: 
            dct[(s,t,k)]='Yes'
            return dct[(s,t,k)]
        ls,lt=len(s),len(t)
        if ls>=lt: #only delete
            dct[(s,t,k)]=appendAndDelete(s[0:-1],t,k-1)
            return dct[(s,t,k)]
        else:
            op1=appendAndDelete(s[0:-1],t,k-1) #delete
            op2=appendAndDelete(s+t[ls],t,k-1)
            if op1=='Yes' or op2=='Yes': dct[(s,t,k)]='Yes'
            else: dct[(s,t,k)]='No'
            return dct[(s,t,k)]
    return appendAndDelete_int(s,t,k)

print(appendAndDelete('abc','def',6))
print(appendAndDelete('hackerhappy','hackerrank',9))
print(appendAndDelete('abc','aba',7))
print(appendAndDelete('ashley','ash',2))