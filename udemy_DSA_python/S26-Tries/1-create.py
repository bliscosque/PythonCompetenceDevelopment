class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.EOS=False  #end of string

class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()

    def insertStr(self, word):
        current=self.root
        for i in word:
            ch=i
            node=current.children.get(ch)
            if node==None:
                node=TrieNode()
                current.children.update({ch:node})
            current=node
        current.EOS=True
        print("OK")

newTrie=Trie()
newTrie.insertStr("APP")
newTrie.insertStr("APPL")