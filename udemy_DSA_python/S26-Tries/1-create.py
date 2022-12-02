class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.EOS=False  #end of string

class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()

    def insertStr(self, word):
        current=self.root
        for ch in word:
            node=current.children.get(ch)
            if node==None:
                node=TrieNode()
                current.children.update({ch:node})
            current=node
        current.EOS=True
        print("OK")

    def searchStr(self, word):
        current=self.root
        for ch in word:
            node=current.children.get(ch)
            if node==None: return False
            current=node
        return current.EOS

def deleteStr(root, word, idx):
    ch=word[idx]
    currentNode=root.children.get(ch)
    canThisNodeBeDeleted=False

    if len(currentNode.children) > 1:
        deleteStr(currentNode, word, idx+1)
        return False
    if idx==len(word)-1:
        if len(currentNode.children)>=1:
            currentNode.EOS=False
            return False
        else: 
            root.children.pop(ch)
            return True
    
    if currentNode.EOS==True:
        deleteStr(currentNode, word, idx+1)
        return False

    canThisNodeBeDeleted=deleteStr(currentNode, word, idx+1)
    if canThisNodeBeDeleted:
        root.children.pop(ch)
        return True
    else: return False

newTrie=Trie()
newTrie.insertStr("APP")
newTrie.insertStr("APPL")
print(newTrie.searchStr("APP"))
print(newTrie.searchStr("APPI"))
print(newTrie.searchStr("AP"))
print()
deleteStr(newTrie.root, "APP",0)
print(newTrie.searchStr("APP"))