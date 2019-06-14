def kra(p):
    return p*p

z = kra(5)
print(z)
def fact(f):
    if f==0:
        return 1
    else:
        return f*fact(f-1)

x = fact(5)
print(x)

#converting to miles
def kilometer(x):
    return 1.6*x

x = int(input())
km = kilometer(x)
print(km)
