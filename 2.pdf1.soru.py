a=0
b=2
c=4
i=0

while i < 4:
    ak=(b+c)/2
    a=ak
    f=a*a*a-2*a*a-5
    if(f<0):
        b=ak
    else:
        c=ak
    i+= 1

print("4 iterasyon sonucu bulunan kok",ak)
print("4 iterasyon sonucu bulunan deger",f)
