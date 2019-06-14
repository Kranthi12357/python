"""sets which is unordered and unindexed"""
sets = {"kranthi","bhagath","kittu","bhagath"}
"""to acess the element"""
print(sets)

"""iteration"""
for i in sets:
    print(i)
"""check if exists"""
if "kranthis" not in sets:
    print("print true")
"""adding items to list"""
sets.add("kavitha")
print(sets)
"""if you wish to add multiple items please use update"""
sets.update(["cooler","washing machine"])
print(sets)
"""remove and discard"""
sets.discard("cooler")# if item not present it will not raise an error
print(sets)
sets.remove("washing machine")# if item not present it will not raise a error
print(sets)
"""move to deletion"""
sets.pop()# we don't know which will be deleted because it is unordered
print(sets)
sets.clear()
print(sets)
del sets
