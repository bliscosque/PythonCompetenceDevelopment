def cavityMap(grid):
    n=len(grid)
    ngrid=grid[:]
    for i in range(1,n-1):
        for j in range(1,n-1):
            el=grid[i][j]
            if el>grid[i-1][j] and el>grid[i][j-1] and el>grid[i][j+1] and el>grid[i+1][j]:
                ngrid[i]=ngrid[i][:j]+'X'+ngrid[i][j+1:]
    return ngrid

print(cavityMap(['989','191','111']))
print(cavityMap(['1112','1912','1892','1234']))
print(cavityMap(['159','483','256']))