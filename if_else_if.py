a = 21
b = 23
c = 22
if a>b:
    if a>c:
        print("a is greater")
    else:
        print(" c is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")
print("enter the height")
x = int(input())
print("enter the weight")
y = int(input())
z = y/(x**2)
if z > 25:
    print("over weight")
else:
    print("under weight")