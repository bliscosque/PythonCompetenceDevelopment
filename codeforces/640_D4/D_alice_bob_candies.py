from collections import deque
def solve():
    n=(input())
    l=[int(i) for i in input().split()]
    deq=deque(l)
    alice=0
    bob=0
    isAlice=False
    moves=1
    alice+=deq.popleft()
    sum_prev=alice
    while len(deq)>0:
        #print(isAlice, alice, bob, moves)
        sum_cur=0
        if isAlice:
            moves+=1
            while sum_cur<=sum_prev:
                candie=deq.popleft()
                alice+=candie
                sum_cur+=candie
                if len(deq)==0: break
            isAlice=False
        else:
            moves+=1
            while sum_cur<=sum_prev:
                #print(sum_cur)
                candie=deq.pop()
                bob+=candie
                sum_cur+=candie
                if len(deq)==0: break
            isAlice=True
        sum_prev=sum_cur
    print(moves, alice, bob)    
        
for _ in range(int(input())):
    solve()