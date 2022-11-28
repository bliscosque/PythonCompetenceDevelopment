#Write a function to find all pairs of an integer array whose sum is equal to a given number.

def pairSum(myList, sum):
    ans=[]
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if myList[i]+myList[j]==sum: ans.append(str(myList[i])+'+'+str(myList[j]))
    return ans



print(pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))
#Output : ['2+5', '4+3', '3+4', '-2+9']