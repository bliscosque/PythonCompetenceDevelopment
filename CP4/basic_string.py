def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

with open('./basic_string_in.txt') as f:
    lines=[]
    while True:
        line=f.readline()
        if line.startswith("......."):
            break
        lines.append(line)
oneLine=' '.join(lines).replace('\n', '')
print(oneLine)
# todas as ocorrencias na string
print([i for i in findall('I', oneLine)])
print([i for i in findall('i', oneLine)])
print([i for i in findall('love', oneLine)])
print([i for i in findall('book', oneLine)])
