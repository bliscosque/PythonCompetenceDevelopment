class Binary_Node:
    def __init__(self,x):
        self.item=x
        self.left=None
        self.right=None
        self.parent=None

    def subtree_iter(A):
        if A.left: yield from A.left.subtree_iter()
        yield A
        if A.right: yield from A.right.subtree_iter()

    def subtree_first(A):
        if A.left: return A.left.subtree_first()
        else: return A
    
    def subtree_last(A):
        if A.right: return A.right.subtree_first()
        else: return A

    def successor(A):
        if A.right: return A.right.subtree_first()
        while(A.parent) and (A is A.parent.right):
            A=A.parent
        return A.parent

    def predecessor(A):
        if A.left: return A.right.subtree_last()
        while(A.parent) and (A is A.parent.left):
            A=A.parent
        return A.parent

    def subtree_insert_before(A,B):
        if A.left:
            A=A.left.subtree_last()
            A.right, B.parent = B,A
        else:
            A.left, B.parent = B,A

    def subtree_insert_after(A,B):
        if A.right:
            A=A.right.subtree_first()
            A.left, B.parent = B,A
        else:
            A.right, B.parent = B,A

    def subtree_delete(A):
        if A.left or A.right:
            if A.left: B=A.predecessor()
            else: B=A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:
            if A.parent.left is A: A.parent.left=None
            else: A.parent.right=None
        return A

class Binary_Tree:
    def __init__(self, Node_Type=Binary_Node):
        self.root=None
        self.size=0
        self.Node_Type=Node_Type

    def __len__(self): return self.size

    def __iter__(self):
        if self.root:
            for A in self.root.subtree_iter(): yield A.item

    def build(self, X):
        A=[x for x in X]
        def build_subtree(A,i,j):
            c=(i+j)//2
            root=self.Node_Type(A[c])
            if i<c:
                root.left = build_subtree(A, i, c - 1)
                root.left.parent = root
            if c<j:
                root.right = build_subtree(A, c + 1, j)
                root.right.parent = root
            return root
        self.root=build_subtree(A, 0, len(A)-1)

    def subtree_rotate_right(self):
        assert self.left
        B, E = self.left, self.right
        A, C = B.left, B.right
        self, B = B, self
        self.item, B.item = B.item, self.item
        B.left, B.right = A, self
        self.left, self.right = C, E
        if A: A.parent = B
        if E: E.parent = self
        # B.subtree_update()
        # D.subtree_update()

    def subtree_rotate_left(self):
        assert self.right
        A, D = self.left, self.right
        C, E = D.left, D.right
        self, D = D, self
        self.item, D.item = D.item, self.item
        D.left, D.right = D, self
        self.left, self.right = A, C
        if A: A.parent = self
        if E: E.parent = D
        # B.subtree_update()
        # D.subtree_update()

    def skew(self):
        return height(self.right) - height(self.left)

    def rebalance(self):
        if self.skew() == 2:
            if self.right.skew() < 0:
                self.right.subtree_rotate_right()
            self.subtree_rotate_left()
        elif self.skew() == -2:
            if self.left.skew() > 0:
                self.left.subtree_rotate_left()
            self.subtree_rotate_right()

    def maintain(self):
        self.rebalance()
        self.subtree_update()
        if self.parent: self.parent.maintain()

    def height(self):
        if A is None: return -1
        return 1+max(height(self.left), height(self.right))

def subtree_print(A):
    if A.left:subtree_print(A.left)
    print(A.item)
    if A.right:subtree_print(A.right)

r=Binary_Node(0)
r.left=Binary_Node(2)
r.left.left=Binary_Node(5)
r.right=Binary_Node(10)
subtree_print(r)
print()
a=[1,2,3,4,5,10]
T=Binary_Tree()
T.build(a)
subtree_print(T.root)