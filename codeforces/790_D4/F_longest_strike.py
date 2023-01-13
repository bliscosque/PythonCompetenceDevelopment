from collections import Counter

def solve():
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    
    #s2=set()
    #print(dct)
    #print(s)
    
    # add only valid elem to s2
    L=[]
    dct=Counter(a)
    for el,v in dct.items():
        if v>=k: L.append(el)
    #print(L)

    # if k==1:
    #     s2=set(a)
    # else: 
    #     dct=Counter(a)
    #     s2={el for el,v in dct.items() if v>=k}
    
    #border cases
    # if len(s2)==0:
    #     print(-1)
    #     return

    # if len(s2)==1:
    #     el=s2.pop()
    #     print(el, el)
    #     return
    
    if len(L)==0:
         print(-1)
         return

    if len(L)==1:
         print(L[0], L[0])
         return

    #s2=sorted(s2)

    L.sort()
    start=0
    cnt=1
    ans=[]
    #print(L)
    for i in range(1,len(L)):
        if cnt+L[start]==L[i]:
            cnt+=1
            continue
        else:
            ans.append((L[start],L[i-1]))
            start=i
            cnt=1
    ans.append((L[start],L[i]))
    maxL=-1
    minAll=maxAll=L[0]
    for (s,e) in ans:
        if e-s>maxL:
            maxL=e-s
            minAll=s
            maxAll=e


    # i=0
    # while i<(len(L)-1):
    #     cnt=1
    #     min_el=L[i]
    #     while i<(len(L)-1):
    #         if L[i]+1==L[i+1]:
    #             cnt+=1
    #             i+=1
    #         else: break
    #     max_el=L[i]
    #     if cnt>long:
    #         long=cnt
    #         minAll=min_el
    #         maxAll=max_el
    #     i+=1

    # for el in s2:
    #     parent=el-1
    #     if parent not in s2:
    #         min_el=el
    #         next_no=el+1
    #         cnt=1
    #         while next_no in s2:
    #             next_no+=1
    #             cnt+=1
    #         if cnt>long:
    #             long=cnt
    #             minAll=min_el
    #             maxAll=min_el+cnt-1
    
    print(minAll,maxAll)

for _ in range(int(input())):
    solve()