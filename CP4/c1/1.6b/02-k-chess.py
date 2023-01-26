def alltries (ans,sc,sl,ec,el,cnt):
    global found
    if found: return
    if cnt==3: 
        #print("Impossible")
        return -1
    if sc==ec and sl==el: 
        print(ans)
        found=True
        return
    x=[1,1,-1,-1]
    y=[1,-1,1,-1]
    for mov in range(len(x)):
        for mul in range(1,9):
            if 0<=(sc+x[mov]*mul)<=8 and 0<=(sl+y[mov]*mul)<=7: 
                ans.append((sc+x[mov]*mul,sl+y[mov]*mul))
                alltries(ans,sc+x[mov]*mul,sl+y[mov]*mul,ec,el,cnt+1)
                del ans[-1]


for _ in range(int(input())):
    sc,sl,ec,el=[i for i in input().split()]
    #want to go from s to e in, at most, 4 moves. "Impossible" otherwise
    sc=ord(sc)-ord('A')
    ec=ord(ec)-ord('A')
    sl=int(sl)-1
    el=int(el)-1
    global found
    found=False

    ans=[]
    alltries(ans,sc,ec,sl,el,0)
    
    