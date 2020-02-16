def palindrom(x,y):
    najveciPalindrom=0
    najveciCinioci=(0,0)
    for i in range(x,y):
        for j in range(i,y):
            p=i*j
            s=str(p)
            if s==s[::-1] and p>najveciPalindrom: #s[0]==s[-1] and s[1]==s[-2] and s[2]==s[-3] and s[3]==s[-4]
                najveciPalindrom=p
                najveciCinioci=(i,j)
    return najveciPalindrom,najveciCinioci

print(palindrom(100,1000))