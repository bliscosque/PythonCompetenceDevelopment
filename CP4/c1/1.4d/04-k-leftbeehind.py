def solve(x,y):
    if x+y==13: print("Never speak again.")
    elif y>x: print("Left beehind.")
    elif x>y: print("To the convention.")
    else: print("Undecided.")
x,y=[int(i) for i in input().split()]
while x!=0 or y!=0:
    solve(x,y)
    x,y=[int(i) for i in input().split()]
