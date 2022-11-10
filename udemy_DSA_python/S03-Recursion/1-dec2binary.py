def dec2bin(num):
    if num==0: return 0
    return num%2+10*dec2bin(num//2)

print(dec2bin(50))