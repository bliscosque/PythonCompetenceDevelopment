# subset=subsequence (que nao é o mesmo de substring, que precisa ser continuo)
def find_subsets(str,ps='',start=0):
    if start==len(str):
        print(ps)
        return
    find_subsets(str,ps,start+1) # does not include
    find_subsets(str,ps+str[start],start+1) # include


find_subsets('abc')