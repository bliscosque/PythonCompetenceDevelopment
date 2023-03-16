def PredictTheWinner(nums):
    def pdwint(nums,s,e,p1,p2,isp1):
        #print(nums,s,e,p1,p2,isp1)
        if s==e:
            if isp1:
                #print(p1+nums[s]>=p2)
                return p1+nums[s]>=p2
            else:
                #print(p1+nums[s]>=p2)
                return p1>=p2+nums[s]
        if isp1:
            op1=pdwint(nums,s+1,e,p1+nums[s],p2,False)
            op2=pdwint(nums,s,e-1,p1+nums[e],p2,False)
            return op1 or op2
        else:
            op1=pdwint(nums,s+1,e,p1,p2+nums[s],True)
            op2=pdwint(nums,s,e-1,p1,p2+nums[e],True)
            return op1 and op2
    
    return pdwint(nums,0,len(nums)-1,0,0,True)

print(PredictTheWinner([1,5,2]))