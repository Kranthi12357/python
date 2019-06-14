list = ["laptop ","mouse","phone"]
list1 = ['lap','mou','phon','phon']
list2 = ['wire',"keyboard",'charger']
print(list)
print(list1)
print(list2)
#operations on the list
"""list is the collection which is ordered and changeable 
allow duplicate elements"""
#1.acess
print(list[1])
#2.replace
list[1]='wire'
print(list)
#3.loop through a list
for i in list:
    print(i)
#4. check if it exist
if 'wire' in list:
    print("exists")
#5. length of a list
print(len(list))
#append
list.append("kranthi")
print(list)
list.insert(1,"bhagath")
print(list)
# remove item
list.remove("kranthi")
print(list)
del list[1]
print(list)
list.pop()#if you mention the index it will delete the mentioned
#index otherwise last is the choice.
print(list)
list.clear()
print(list)
del list
print(list)
#copy of a list
list3 = list1.copy()
print(list3)
# sorting the list
list1.sort()
print(list1)
#reverse list
list1.reverse()
print(list1)
#index element
l = list1.index("phon")
print(l)
#extend
list1.extend(list2)
print(list1)
#count
print(list1.count("phon"))