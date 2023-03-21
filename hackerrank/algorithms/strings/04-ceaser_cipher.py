def caesarCipher(s, k):
    ab='abcdefghijklmnopqrstuvwxyz'
    abU='abcdefghijklmnopqrstuvwxyz'.upper()
    l=len(ab)
    ans=''
    for ch in s:
        if ch in ab: 
            ans+=ab[(ab.index(ch)+k)%l]
        elif ch in abU:
            ans+=abU[(abU.index(ch)+k)%l]
        else:
            ans+=ch
    return ans

print(caesarCipher('middle-Outz',2))