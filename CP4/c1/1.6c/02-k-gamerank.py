line=input()
rank=25
stars=0
for idx,ch in enumerate(line):
    if rank==0:
        continue
    bonus=False
    if ch=='W':
        stars+=1
        if 6<=rank<=25 and line[idx-1]=='W' and line[idx-2]=='W':
            stars+=1 #Bonus
            bonus=True
        if 1<=rank<=10 and stars>=5:
            rank-=1
            stars=1
            if bonus: stars+=1
        elif 11<=rank<=15 and stars>=4:
            rank-=1
            stars=1
            if bonus: stars+=1
        elif 16<=rank<=20 and stars>=3:
            rank-=1
            stars=1
            if bonus: stars+=1
        elif 21<=rank<=25 and stars>=2:
            rank-=1
            stars=1
            if bonus: stars+=1

    if ch=='L':
        if 1<=rank<=20:
            stars-=1
            if stars<0:
                rank+=1
                if rank>20: rank=20
                if 1<=rank<=10: stars=4
                elif 11<=rank<=15: stars=3
                elif 16<=rank<=20: stars=2
                elif 21<=rank<=25: stars=1


if rank==0:
    print('Legend')
else: print(rank)
        