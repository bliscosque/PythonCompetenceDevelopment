#https://www.geeksforgeeks.org/find-the-kth-number-which-is-not-divisible-by-n/
import math
def solve():
    n,k=[int(i) for i in input().split()]
    print(k+(k-1)//(n-1))
        
for _ in range(int(input())):
    solve()