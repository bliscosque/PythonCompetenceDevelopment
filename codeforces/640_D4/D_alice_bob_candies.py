from collections import deque
def solve():
    n=(input())
    l=[int(i) for i in input().split()]
    deq=deque(l)
    alice=0
    bob=0
    isAlice=True
    moves=0
    while len(deq)>0:
        if isAlice:
            alice+=deq.popleft()
            if alice>bob:
                isAlice=False
                moves+=1
        else:
            bob+=deq.pop()
            if alice<bob:
                isAlice=True
                moves+=1
        print(isAlice, alice, bob, moves)
    print(moves, alice, bob)    
        
for _ in range(int(input())):
    solve()