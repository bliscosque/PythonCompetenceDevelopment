from math import floor


def bin_add(a,b):
    max_len=max(len(a),len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    ans=''
    c=0 #carry
    for i in range(max_len-1,-1,-1):
        val=int(a[i])+int(b[i])+c
        c=(val)//2
        d=(val)%2
        ans+=str(d)
    if (c==1):
        ans+='1'
    ans=ans[::-1]
    return ans

print(bin_add('1011','1110'))