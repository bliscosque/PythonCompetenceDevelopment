txt=input().rstrip()
secret="PER"
pos=0
cnt=0
for ch in txt:
    #print(ch, secret[pos])
    if ch!=secret[pos]: cnt+=1
    pos=(pos+1)%3
print(cnt)