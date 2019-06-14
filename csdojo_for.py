x = list(range(1,100))
print(x)
total = 0
for i in x:
    if i%3 == 0 or i %5 ==0 :
        total = total+i
else:
    print(total)

