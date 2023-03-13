def plusMinus(arr):
    p,n,z=0,0,0
    for i in arr:
        if i==0: z+=1
        elif i>0: p+=1
        else: n+=1
    if len(arr)>0:
        print(f'{p/len(arr):.6f}')
        print(f'{n/len(arr):.6f}')
        print(f'{z/len(arr):.6f}')
    else:
        for i in range(3):
            print("0.000000")

arr=[1,1,0,-1,-1]
plusMinus(arr)