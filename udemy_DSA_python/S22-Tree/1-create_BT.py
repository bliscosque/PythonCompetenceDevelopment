class TreeNode:
    def __init__(self, data):
        self.data=data
        self.lChild=None #left
        self.rChild=None #right

    def __str__(self, level=0):
        ret=" "*level+str(self.data) + "\n"
        for child in [self.lChild, self.rChild]:
            if child is not None: ret+=child.__str__(level+1)
        return ret

    
        
    
tree=TreeNode('Bebidas')
print(tree)