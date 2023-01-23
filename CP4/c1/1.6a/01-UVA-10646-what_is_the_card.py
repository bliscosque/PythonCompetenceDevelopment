def solve():
    cards=[s for s in input().split()]
    new_pile=[]
    y=0
    for _ in range(3):
        top=cards[-1]
        if '2'<=top[0]<='9':
            x=int(top[0])
        else: 
            x=10
        y+=x
        cards_to_remove=10-x+1
        new_pile+=cards[-cards_to_remove]
        del cards[-cards_to_remove]
    new_pile+=cards
    print(new_pile[24])

for _ in range(int(input())):
    solve()