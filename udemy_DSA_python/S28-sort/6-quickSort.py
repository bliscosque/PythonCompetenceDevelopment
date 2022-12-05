def swap(my_list, idx1, idx2):
    my_list[idx1],my_list[idx2]=my_list[idx2],my_list[idx1]

def pivot(my_list, pivot_idx, end_idx):
    swap_idx=pivot_idx
    for i in range(pivot_idx+1,end_idx+1):
        if my_list[i]<my_list[pivot_idx]:
            swap_idx+=1
            swap(my_list, swap_idx, i)
    swap(my_list, pivot_idx, swap_idx)
    return swap_idx

def quickSort(my_list, l, r):
    if l>=r: return
    pivot_idx=pivot(my_list, l, r)
    quickSort(my_list, l,pivot_idx-1)
    quickSort(my_list, pivot_idx+1, r)

cList=[2,1,6,3,5,6,88]
#print(pivot(cList, 0, len(cList)-1))
quickSort(cList, 0, len(cList)-1)
print(cList)