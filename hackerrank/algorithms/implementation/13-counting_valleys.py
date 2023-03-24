def countingValleys(steps, path):
    pos=0
    ans=0
    for ch in path:
        if ch=='D':
            if pos==0: ans+=1
            pos-=1
        else:
            pos+=1
    return ans

print(countingValleys(8,'DDUUUUDD'))
print(countingValleys(8,'UDDDUDUU'))
