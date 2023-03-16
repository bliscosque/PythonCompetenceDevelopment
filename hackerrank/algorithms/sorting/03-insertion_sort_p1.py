def insertionSort1(n, arr):
    el=arr[-1]
    idx=n-1
    while arr[idx-1]>el:
        arr[idx]=arr[idx-1]
        idx-=1
        if idx==-1: 
            idx=0
            break
        for x in arr:
            print(x,end=' ')
        print()

    arr[idx]=el
    for x in arr:
        print(x,end=' ')
    print()



#insertionSort1(5,[1,2,4,5,3])
insertionSort1(10,[2, 3, 4, 5, 6, 7, 8, 9, 10, 1])