
class segment_tree:
    def __init__(self,n) -> None:
        self.n=n
        self.st=[0]*4*n # segment tree array. Max size is always 4*n
        self.lazy=[0]*4*n # for lazy propagation
        
    def build(self,a, start=0,end=None,node=0):
        if end==None: end=len(a)-1 # first call... build from start to end

        # base case (start==end)
        if start==end:
            self.st[node]=a[start]
            return

        mid=(start+end)//2
        # left subtree (start,mid)
        self.build(a, start,mid,2*node+1) # 2*node+1 is left node

        # right subtree (mid+1,end)
        self.build(a, mid+1,end,2*node+2) # 2*node+2 is right node

        # for summation -> calculate the sum base on left and right children
        self.st[node]=self.st[node*2+1]+self.st[node*2+2]

    #def query(self,)
    def query(self,l,r, start=0, end=None, node=0):
        if end==None: end=self.n-1 #fist call... check all 
        
        if start>r or end<l: return 0 # non overlapping case

        # pending updates from lazy subtree segment
        if self.lazy[node]!=0: 
            self.st[node]+=self.lazy[node]*(end-start+1) # update ST with proper value
            if start!=end: # not a leaf node... propagate the lazy tree to children
                self.lazy[2*node+1]+=self.lazy[node]
                self.lazy[2*node+2]+=self.lazy[node]
            self.lazy[node]=0

        if start>=l and end <=r: return self.st[node] # full overlapping case

        # partial case
        mid=(start+end)//2
        ql=self.query(l,r,start,mid,2*node+1) # query left subtree
        qr=self.query(l,r,mid+1,end,2*node+2) # query right subtree
        # for summation -> return sum of both subqueries
        return ql+qr 

    def update(self,idx_l, idx_r,val,start=0,end=None,node=0):
        if end==None: end=self.n-1 #start with all the array

        if start>idx_r or end<idx_l: return # non overlapping case

        # pending updates from lazy subtree segment
        if self.lazy[node]!=0: 
            self.st[node]+=self.lazy[node]*(end-start+1) # update ST with proper value
            if start!=end: # not a leaf node... propagate the lazy tree to children
                self.lazy[2*node+1]+=self.lazy[node]
                self.lazy[2*node+2]+=self.lazy[node]
            self.lazy[node]=0

        if start>=idx_l and end <=idx_r:  # full overlapping case
            self.st[node] += val*(end-start+1)
            if start!=end:
                self.lazy[2*node+1]+=val
                self.lazy[2*node+2]+=val
            return

        # partial case
        mid=(start+end)//2
        self.update(idx_l,idx_r,val,start,mid,2*node+1) # query left subtree
        self.update(idx_l,idx_r,val,mid+1,end,2*node+2) # query right subtree
        self.st[node]=self.st[node*2+1]+self.st[node*2+2] 
        
         

a=[1,2,3,4,5,6,7,8]
st=segment_tree(len(a))
st.build(a)
# print(st.st)
print(st.query(0,4))
st.update(0,1,10)
print(st.query(0,4))
# print(st.query(2,6))
# st.update(2,20)
# print(st.query(0,4))
