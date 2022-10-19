maxValue=100000
fr = [0]*maxValue #frequency matrix - how many times found a number
#desvantagem: apenas elementos até maxValue

a=[7,3,1,3,2,7]
cnt=0 # conta elementos distintos
for i in a:
    if fr[i]==0: cnt+=1
    fr[i]+=1
print("Ha: ", cnt, "elementos distintos")
