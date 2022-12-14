# substring (ou factor) requer que caracteres sejam consecutivos, ao contrario de uma nocao mais geral: subsequence
#1. anagrams - find words that are anagram of each other
input="below the car is a rat drinking cider and bending its elbow while this thing is an arc that can act like a cat which cried during the night caused by pain in its bowel"
# output: {bowel below elbow}, {arc car}, {night thing}, {cried cider}, {act cat}
def anagram(S):
    d={}
    for word in S:
        s=''.join(sorted(word))
        if s in d:
            d[s].append(word)
        else:
            d[s]=[word] #adiciona a uma "assinatura" ja existente
    return [d[s] for s in d if len(d[s])>1]
print(anagram(set(input.split())))    

