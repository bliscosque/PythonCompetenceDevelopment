
class segment_tree:
    def __init__(self,n) -> None:
        self.n=n
        self.st=[0]*4*n # segment tree array. Max size is always 4*n
        
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
        if start>=l and end <=r: return self.st[node] # full overlapping case

        # partial case
        mid=(start+end)//2
        ql=self.query(l,r,start,mid,2*node+1) # query left subtree
        qr=self.query(l,r,mid+1,end,2*node+2) #query right subtree
        # for summation -> return sum of both subqueries
        return ql+qr 

    def update(self,idx,val,start=0,end=None,node=0):
        if end==None: end=self.n-1 #start with all the array
        # base case
        if start==end:
            self.st[node]=val
            return

        mid=(start+end)//2
        if idx<=mid: #left subtree
            self.update(idx,val,start,mid,2*node+1)
        else:
            self.update(idx,val,mid+1,end,2*node+2)
        #update ancestor... again for sum
        self.st[node]=self.st[node*2+1]+self.st[node*2+2]

a=[1,2,3,4,5,6,7,8]
st=segment_tree(len(a))
st.build(a)
st.query(0,4)
#print(st.st)
print(st.query(0,4))
st.update(4,10)
print(st.query(2,6))
st.update(2,20)
print(st.query(0,4))
