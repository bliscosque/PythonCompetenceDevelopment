def pangrams(s):
    s=s.lower()
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        if ch not in s: return 'not pangram'
    return 'pangram'
    
print(pangrams('We promptly judged antique ivory buckles for the next prize'))
print(pangrams('We promptly judged antique ivory buckles for the prize'))