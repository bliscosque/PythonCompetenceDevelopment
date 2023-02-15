#given 2 str, one big and one small, find the smallest window in the big str that contains all chars of the small str
# - window can have additional chars than required
# - if small str has duplicates, those duplicates must be present with same or higher count in window

import math
from collections import defaultdict
def strWindow(s,p):
    #fBig=[0]*256
    fp=defaultdict(int) #valor padrao=0
    fs=defaultdict(int)
    for c in p:
        fp[c]+=1
    
    cnt=0
    start=0
    start_idx=-1 # best window idx
    min_so_far=math.inf
    for i in range (len(s)):
        ch=s[i]
        fs[ch]+=1
        
        #how many  chars were matched until now
        if fp[ch]!=0 and fs[ch]<=fp[ch]: cnt+=1
        #all chars are found... start contracting
        if cnt==len(p):
            while fp[s[start]]==0 or fs[s[start]]>fp[p[start]]:
                fs[s[start]]-=1
                start+=1
            window_size=i-start+1
            if window_size<min_so_far:
                min_so_far=window_size
                start_idx=start
    if start_idx==-1:
        return "No window found"
    return s[start_idx:start_idx+min_so_far]




print(strWindow("hello","lol")) #llo
print(strWindow("fizzbuzz","fuzz")) #fizzbu