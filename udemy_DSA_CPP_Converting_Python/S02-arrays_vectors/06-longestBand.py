# Given an array containing N integers, find the len of the longest band.
# A band is defined as a subseq. which can be reordered in such a manner all elem appear consecutive (ie with absolute difference of 1 between neighbouring elem)

def largest_band(arr):
    n=len(arr)
    s=set(arr)
    largLen=1
    for el in s:
        parent=el-1
        if parent not in s:
            next_no=el+1
            cnt=1
            while next_no in s:
                next_no+=1
                cnt+=1
            largLen=max(largLen,cnt)
    return largLen

arr =[1, 9, 3, 0, 18, 5, 2, 4, 10, 7, 12, 6] # Contem elementos: 0,1,2,3,4,5,6,7 
print(largest_band(arr))