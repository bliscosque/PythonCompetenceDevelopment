import fileinput
l0=[ch for ch in '`123456789-=']
l1=[ch for ch in 'QWERTYUIOP[]\\']
l2=[ch for ch in "ASDFGHJKL;'"]
l3=[ch for ch in 'ZXCVBNM,./']

def conv(line):
    nline=''
    for ch in line:
        if ch in l0: nline+=l0[l0.index(ch)-1]
        elif ch in l1: nline+=l1[l1.index(ch)-1]
        elif ch in l2: nline+=l2[l2.index(ch)-1]
        elif ch in l3: nline+=l3[l3.index(ch)-1]
        else: nline+=ch
    return nline

lines=[]
for line in fileinput.input():
    lines.append(line.rstrip())
for line in lines:
    print(conv(line))