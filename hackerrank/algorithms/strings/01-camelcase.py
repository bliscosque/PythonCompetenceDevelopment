def camelcase(s):
    cnt=1
    for ch in s:
        if 'A'<=ch<='Z': cnt+=1
    return cnt

print(camelcase('saveChangesInTheEditor'))