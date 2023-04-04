def workbook(n, k, arr):
    page=1
    ans=0
    for i in range(n):
        probs=arr[i]
        p_start=1
        while p_start<=probs:
            if p_start<=i+1<p_start+k: ans+=1
            p_start+=k
            page+=1
    return ans
        

    
print(workbook(2,3,[4,2]))
print(workbook(5, 3, [4, 2, 6, 1, 10]))