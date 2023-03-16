# given a number N and a modern phone keypad. Find out all possible strings generated using that #
def phone_keypad(s, output='',i=0):
    kp=["","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
    if i==len(s):
        print(output)
        return
    cur_digit=int(s[i])
    if cur_digit in [0,1]:
        phone_keypad(s,output,i+1)
    for k in range(len(kp[cur_digit])):
        phone_keypad(s,output+kp[cur_digit][k],i+1)

phone_keypad("23") #AD,AE,AF,BD,BE,BF,CD,CE,CF