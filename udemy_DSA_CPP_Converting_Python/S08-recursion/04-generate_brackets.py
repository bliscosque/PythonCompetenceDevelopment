def generateBrackets(output,n,open,close,i):
    if i==2*n:
        print(output)
    if open<n:
        generateBrackets(output+'(',n,open+1,close,i+1)
    if close<open:
        generateBrackets(output+')',n,open,close+1,i+1)

generateBrackets('',3,0,0,0)