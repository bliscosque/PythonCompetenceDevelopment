import bisect
def introTutorial(V, arr):
    return bisect.bisect_left(arr,V)

print(introTutorial(4,[1, 4, 5, 7, 9, 12]))