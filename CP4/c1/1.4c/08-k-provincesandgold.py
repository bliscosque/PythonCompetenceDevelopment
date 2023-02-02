G,S,C=[int(i) for i in input().split()]
# G+S+C <= 5

v=G*3+S*2+C
if v>=8:VP='Province'
elif v>=5: VP='Duchy'
elif v>=2: VP='Estate'
else: VP=''
if v>=6: TC='Gold'
elif v>=3: TC='Silver'
else: TC='Copper'

if VP!='':
    print(f'{VP} or ', end='')
print(TC)