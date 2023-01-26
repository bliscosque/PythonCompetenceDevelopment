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

#2. text on 9 keys
# dado uma sequencia de numeros, encontrar a palavra relacionada a esses numeros (se digitadas num celular com T9)
input=2665687 # output: bonjour
t9 = "22233344455566677778889999" 
#     abcdefghijklmnopqrstuvwxyz mapping on the phone
def letter_to_digit(x): 
    assert 'a' <= x <= 'z' 
    return t9[ord(x) - ord('a')]
def code_word(word): 
    return ''.join(map(letter_to_digit, word))
def predictive_text(dic): 
    # total_weight[p] = total weight of words having prefix p 
    total_weight = {} 
    for word, weight in dic: 
        prefix = "" 
        for x in word: 
            prefix += x 
            if prefix in total_weight: 
                total_weight[prefix] += weight
            else: 
                total_weight[prefix] = weight
    # prop[s] = prefix to display for s 
    prop = {} 
    for prefix in total_weight: 
        code = code_word(prefix) 
        if (code not in prop or total_weight[prop[code]] < total_weight[prefix]):
            prop[code] = prefix 
            return prop
def propose(prop, seq): 
    if seq in prop: 
        return prop[seq]
    return None



