def taumBday(b, w, bc, wc, z):
    wct=wc*w
    bct=bc*b
    #print(wct,bct)
    if bc+z<=wc:
        wct=(bc+z)*w
    if wc+z<=bc:
        bct=(wc+z)*b
    return wct+bct

print(taumBday(3,5,3,4,1))
print(taumBday(10,10,1,1,1))
print(taumBday(5,9,2,3,4))
