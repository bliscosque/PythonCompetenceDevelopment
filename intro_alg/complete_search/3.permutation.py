def permut(nums):
    perm=[]
    n=len(nums)
    chosen=[False]*n
    
    def permut_int():
        nonlocal n
        if len(perm)==n:
            print(perm)
        else:
            for i in range(n):
                if chosen[i]: continue

                chosen[i]=True
                perm.append(nums[i])
                permut_int()
                chosen[i]=False
                perm.pop()
                
    permut_int()
permut([1,2,3])