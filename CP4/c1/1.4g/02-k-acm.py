line=input()
pok=[]
ptime={}
while '-1' not in line:
    t,p,a=line.split()
    t=int(t)
    if a=='right':
        pok.append(p)
        if p in ptime:
            ptime[p]+=t
        else:
            ptime[p]=t
    else:
        if p in ptime:
            ptime[p]+=20
        else: 
            ptime[p]=20    
    line=input()
#print(pok,ptime)
ttime=0
for p in pok:
    ttime+=ptime[p]
print (len(pok), ttime)