def designerPdfViewer(h, word):
    max = 0
    for i in word:
        if h[ord(i)-97]>max:
            max = h[ord(i)-97]
    return max*len(word)
