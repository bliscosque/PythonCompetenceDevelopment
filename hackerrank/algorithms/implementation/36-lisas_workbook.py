def workbook(n, k, arr):
    page=1
    ans=0
    for i in range(n):
        probs=arr[i]
        p_start=1
        p_end=p_start+k-1
        if p_end>probs: p_end=probs

        while p_start<=probs:
            #print(page,p_start,p_end)

            if p_start<=page<=p_end: ans+=1

            p_start+=k
            p_end=p_start+k-1
            if p_end>probs: p_end=probs
            page+=1

    return ans
        

    
print(workbook(2,3,[4,2]))
print(workbook(5, 3, [4, 2, 6, 1, 10]))