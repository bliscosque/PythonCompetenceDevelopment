def angryProfessor(k, a):
    onTime=sum(1 for i in a if i<=0)
    #print(onTime)
    return ('YES' if onTime < k else 'NO')


print(angryProfessor(3,[-2,-2,0,1,2]))
print(angryProfessor(3,[-1,-3,4,2]))
print(angryProfessor(2,[0,-1,2,1]))