s = {1,"kranthi","hello"}
for x in s:
    print(x)

g = [1,2,3,4,5,4]

e = set()
for i in g:
    e.add(i)

print(e)

f = []
for i in e:
    f.append(i)
print(f)


g = [1,2,3,5,5,7,4,3,1]
s = set()

for i in g:
    s.add(i)
total = 0
for i in s:
    total = total + i
print(s)
print(total)