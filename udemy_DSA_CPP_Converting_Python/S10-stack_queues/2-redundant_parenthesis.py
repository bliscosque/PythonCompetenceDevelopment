from collections import deque
def checkRedundant(str):
    s=deque()
    for ch in str:
        if ch!=')':
            s.append(ch) # a,b, + , - , ( ....
        else:
            op_found=False
            while len(s)>0 and s[-1]!='(':
                top=s[-1]
                if top in ['+','-','*','/']:
                    op_found=True
                s.pop()
            s.pop() # pop the opening bracked after the loop if over
            if op_found==False: return True
    return False

s="((a+b)+c) + ((d*e))"
print(checkRedundant(s))
s="((a+b)+c) + (d*e)"
print(checkRedundant(s))