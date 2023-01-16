def solve():
    input()
    lines=[]
    for _ in range(8):
        lines.append(input())
    #print(lines)
    has_2_b4=False
    for i in range(8):
        if not has_2_b4 and lines[i].count('#')==2: 
            has_2_b4=True
            continue
        if has_2_b4 and lines[i].count('#')==1: 
            ans_c=i
            ans_l=lines[i].index('#')
            break
    
    print(ans_c+1, ans_l+1)

for _ in range(int(input())):
    solve()