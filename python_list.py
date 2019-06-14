#csdojo list
lis = ['kranthi',1,3,4]
print(lis)
lis.append('kra')
print(lis)
x = lis.index(1)
print(lis[1])
del lis[3]
print(lis)
list1 = lis.copy()
print(list1)
s = lis.count('kra')
print(s)
lis.remove('kra')
lis.remove('kranthi')
print(lis)
for i in lis:
    print(i)