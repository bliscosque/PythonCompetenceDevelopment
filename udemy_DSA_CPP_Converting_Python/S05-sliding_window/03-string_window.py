#given 2 str, one big and one small, find the smallest window in the big str that contains all chars of the small str
# - window can have additional chars than required
# - if small str has duplicates, those duplicates must be present with same or higher count in window

import math
from collections import defaultdict
def strWindow(sBig,sSmall):
    #fBig=[0]*256
    fSmall=defaultdict(int) #valor padrao=0
    fBig=defaultdict(int)
    for c in sSmall:
        fSmall[c]+=1
    
    cnt=0
    start=0
    start_idx=-1 # best window idx
    min_so_far=math.inf
    for i in range (len(sBig)):
        ch=sBig[i]
        fBig[ch]+=1
        
        #how many  chars were matched until now
        if fSmall[ch]!=0 and fBig[ch]<=fSmall[ch]: cnt+=1
        #all chars are found... start contracting
        if (cnt==len(sSmall)):
            while fSmall[sSmall[start]]==0 or fBig[sBig[start]]>fSmall[sSmall[start]]:
                fBig[sBig[start]]-=1
                start+=1
            window_size=i-start+1
            if window_size<min_so_far:
                min_so_far=window_size
                start_idx=start
    if start_idx==-1:
        return "No window found"
    return sBig[start_idx:start_idx+min_so_far]




print(strWindow("hello","lol")) #llo
print(strWindow("fizzbuzz","fuzz")) #fizzbu