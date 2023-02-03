# Dada uma str, encontre uma funcao que encontre a maior substring com caracteres unicos (nao duplicados)

def uniqueSubstr(s):
    dct={}
    l=0
    n=len(s)
    ans=(0,0)
    for r in range(n):
        el=s[r]
        #print(el,l,r,dct,ans)
        if el not in dct:
            dct[el]=r
            if (ans[1]-ans[0])<(r-l): ans=(l,r)
        else:
            for k in range(l,dct[el]+1):
                #print(f"removing {k} {s[k]}")
                if s[k] in dct: del dct[s[k]]
                l=k
            l+=1
    return s[ans[0]:ans[1]+1]





print(uniqueSubstr("prateekbhaiya")) # ekbhaiy
print(uniqueSubstr("aabcb")) # abc