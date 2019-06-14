for i in range(1,10):
    if i == 4:
        break
    print(i)
for i in range(1,5):
    if i == 3:
        continue
    print(i)
i = 1
while i < 4:
    if i == 3:
         break
    print(i)
    i = i+1
l = list(range(1,5))
print(l)
total = 0
for i in l:
    total = total+i
print(total)
while i < len(l) and l[i] > 0:
    total = total + l[i]
    i = i+1
print(total)
tota = 0
j =0
while j < len(l):
    if l[j] > 0:
        tota = tota + l[j]
    j = j+1
print(tota)
print("addition of negative numbers")
total = 0
i = 0
m = [1,2,3,4,-1,-4,-5,-6,-8]
while i < len(m):
    if m[i] < 0:
        total = total + m[i]
    i = i+1
print(total)

if 3>5:
    print("5 is greater")
    print("3 is lesser")
print("5 is ")
i = 0
t =0
while i<len(m):
    if m[i] > 0:
        t = t + m[i]
    i = i+1

print(t)