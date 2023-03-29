def designerPdfViewer(h, word):
    m=0
    for ch in word:
        p=ord(ch)-ord('a')
        m=max(m,h[p])
        #print(m)
    return len(word)*m

print(designerPdfViewer([1,3,1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],'abc'))
print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7], 'zaba'))