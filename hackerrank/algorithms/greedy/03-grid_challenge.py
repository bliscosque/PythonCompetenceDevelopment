def gridChallenge(grid):
    n_grid=[]
    for l in grid:
        n_grid.append(sorted(l))
    #print(n_grid)
    for i in range(len(n_grid[0])):
        c=''
        for j in range(len(n_grid)):
            c+=n_grid[j][i]
        #print(c,sorted(c))
        if c!=''.join(sorted(c)): return 'NO'
    return 'YES'



print(gridChallenge(['abc','ade','efg']))
print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))
print(gridChallenge(['kc','iu'])) # YES
print(gridChallenge(['uxf','vof','hmp'])) #NO