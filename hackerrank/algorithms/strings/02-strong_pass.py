def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    nn=nl=nu=ns=0
    for ch in password:
        if ch in numbers: nn+=1
        elif ch in lower_case: nl+=1
        elif ch in upper_case: nu+=1
        elif ch in special_characters: ns+=1

    ans=0
    if nn<1: ans+=1 
    if nl<1: ans+=1
    if nu<1: ans+=1
    if ns<1: ans+=1
    if (n+ans)<6: 
        ans=6-n
    return ans
    
    
print(minimumNumber(3,'Ab1'))
print(minimumNumber(5,'2bbbb'))
print(minimumNumber(5,'2bb#A'))
print(minimumNumber(11,'#HackerRank'))