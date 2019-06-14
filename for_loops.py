for i in range(1,10,3):
    print(i)
list = ['kranthi','bhagath','kittu','bunny']
for i in list:
    if i == 'kittu':
        break
    print(i)

for i in "kranthi":
    print(i)
for i in list:
    if i == 'kittu':
        continue
    print(i)

for i in "kranthi":
    print(i)
else:
    print("sucessfully finished")