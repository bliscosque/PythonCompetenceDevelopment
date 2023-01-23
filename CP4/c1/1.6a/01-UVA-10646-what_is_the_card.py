def solve(i):
    cards=[s for s in input().split()]
    hands=cards[-25:]
    del cards[-25:]
    #print(hands)
    #print(cards)
    y=0
    for _ in range(3):
        top=cards[-1]
        #print(top)
        if '2'<=top[0]<='9':
            x=int(top[0])
        else: 
            x=10
        y+=x
        cards_to_remove=10-x+1
        del cards[-cards_to_remove:]
    cards+=hands
    print(f'Case {i+1}: {cards[y-1]}')

for i in range(int(input())):
    solve(i)