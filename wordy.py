def proteins(strand):
    dio={"AUG" :"Methionine","UUU":"Phenylalanine", "UUC":"Phenylalanine","UUA":"Leucine", "UUG":"Leucine","UCU":"Serine", "UCC":"Serine", "UCA":"Serine", "UCG"	:"Serine",
"UAU":"Tyrosine", "UAC"	:"Tyrosine",
"UGU":"Cysteine", "UGC":"Cysteine",
"UGG":"Tryptophan"}
    x=3
    m=[]
    empty=[]
    if len(strand)>3:
        for i in range(0,len(strand),3):
            m.append(strand[i:-1]) if x==len(strand) else m.append(strand[i:x])
            x+=3
    else:
        m.append(strand)
    print(m)
    for i in m:
        if i not in dio :
            break
        if i!="UAA" or "UAG" or "UGA":
            empty.append(dio[i])
        elif i=="UAA" or "UAG" or "UGA" :
            break
    return empty
print(proteins("UUUUUU"))