# Given a ladder with N steps. You can take a jump of 1,2 or 3 step each time.
# Find the # of ways to climb the ladder.

def countWays(n):
    if n<0: return 0
    if n==0: return 1
    return countWays(n-1)+countWays(n-2)+countWays(n-3)

print(countWays(4)) #7