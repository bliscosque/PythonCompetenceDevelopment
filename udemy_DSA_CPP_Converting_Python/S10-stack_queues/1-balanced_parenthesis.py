#obs: implementing s stack using deque
from collections import deque

def isBalanced(input):
    s=deque()
    for ch in input:
        #print(ch)
        #print(s)
        if ch in ['(','[','{']:
                  s.append(ch)
        elif ch==')':
              if len(s)>0 and s.pop()=='(': continue
              else: return False
        elif ch==']':
              if len(s)>0 and s.pop()=='[': continue
              else: return False
        elif ch=='}':
              if len(s)>0 and s.pop()=='{': continue
              else: return False
    if len(s)==0: return True
    return False                

s='{ a + (b+c) + ([d+e]*f)) } + k'
print(isBalanced(s))
s='{ a + (b+c) + ([d+e]*f) } + k'
print(isBalanced(s))