import fileinput
tc=1
for line in fileinput.input():
    note,tonality=line.split()
    if len(note)>1:
        nnote=''
        if note[1]=='b':
            if note[0]=='A': nnote='G'
            else: nnote=chr(ord(note[0])-1)
            nnote+='#'
        else:
            if note[0]=='G': nnote='A'
            else: nnote=chr(ord(note[0])+1)
            nnote+='b'
        print(f"Case {tc}: {nnote} {tonality}")
    else: 
        print(f"Case {tc}: UNIQUE")
    tc+=1