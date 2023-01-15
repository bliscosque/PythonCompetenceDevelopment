# given an arr of pos int, where each elem represents the max no of steps you can jump forward in the arr.
# find the min jumps needed to reach the final idx
import math

def arrJumps(arr,dct={}):
    #print(arr)
    l=len(arr)
    if l in dct: return dct[l]
    if l==1: return 0
    cur=arr[0]
    opc=math.inf
    for i in range(1,cur+1):
        if l-i>0:
            opc=min(opc,1+arrJumps(arr[i:],dct))
    #print(opc)
    dct[l]=opc
    return opc        

input=[3,4,2,1,2,3,10,1,1,1,2,5] # 4 (3->4->2->7->5)
print(arrJumps(input))
