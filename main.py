def HCF(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a==b:
        return a
    if a>b:
        return HCF(a-b,b)
    return HCF(a,b-a)
a=108
b=24
if HCF(a,b):
    print("HCF or GCD of",a,"and",b,"is",HCF(a,b))
else:
    print("Not found")