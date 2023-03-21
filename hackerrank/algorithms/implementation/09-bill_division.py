def bonAppetit(bill, k, b):
    b_actual=(sum(bill)-bill[k])/2
    if b-b_actual<=0.001:
        print('Bon Appetit')
    else:
        print(int(b-b_actual))

bonAppetit([3,10,2,9],1,12)
bonAppetit([3,10,2,9],1,7)