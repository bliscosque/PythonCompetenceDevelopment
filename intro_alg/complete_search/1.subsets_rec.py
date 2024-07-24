subset=[]
n=4
def sset(k):
    if k==n:
        print(subset)
    else:
        #not include k
        sset(k+1) 

        #or include k
        subset.append(k)
        sset(k+1)
        subset.pop() # backtracking

sset(0)

