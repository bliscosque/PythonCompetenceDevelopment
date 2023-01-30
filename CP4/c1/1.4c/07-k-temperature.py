x,y=[int(i) for i in input().split()]
# Derivando a formula do problema: A=-x/(y-1)
if y-1<.5:
    if x==0: print("ALL GOOD")
    else: print("IMPOSSIBLE") 
else: print(-x/(y-1))