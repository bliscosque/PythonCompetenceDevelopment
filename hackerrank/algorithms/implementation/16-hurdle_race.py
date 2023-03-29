def hurdleRace(k, height):
    m=max(height)
    if m>k: return m-k
    else: return 0
print(hurdleRace(1,[1,2,3,3,2]))
print(hurdleRace(4, [1,6,3,5,2]))
print(hurdleRace(7, [2,5,4,5,2]))