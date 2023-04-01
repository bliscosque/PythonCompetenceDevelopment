def permutationEquation(p):
    ans=[0]*len(p)
    for i in p:
        pp=p.index(i)+1
        ppp=p.index(pp)+1
        #print(i,pp,ppp)
        ans[i-1]=ppp
    return ans



print(permutationEquation([5,2,1,3,4]))
print(permutationEquation([2,3,1]))