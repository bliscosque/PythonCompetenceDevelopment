def acmTeam(topic):
    n=len(topic)
    max=0
    ans=0
    for i in range(n-1):
        for j in range(i+1,n):
            cnt=0
            for k in range(len(topic[0])):
                if topic[i][k]=='1' or topic[j][k]=='1':
                    cnt+=1
            #print(topic[i],topic[j],max,ans,cnt)
            if cnt>max:
                max=cnt
                ans=1
            elif cnt==max:
                ans+=1  
    return[max,ans]
print(acmTeam(['10101','11110','00010']))
print(acmTeam(['10101','11100','11010','00101']))
