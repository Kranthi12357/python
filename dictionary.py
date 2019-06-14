dict = {
    "name":"kranthi",
    "college":"cbit",
    "location": "hyderabad",
    "roll_no": 39
}
"""print this tuple"""
print(dict)
"""acessing the elements"""
print(dict["name"])

for i in dict.keys():
    print(dict[i])
for i in dict.values():
    print(i)
for i in dict.keys():
    print(i)
"""change the name"""
dict["name"]="bhagath"
print(dict)
"""print keys and values"""
for i,j in dict.items():
    print(i ,j)
"""check if key exist"""
if "roll_no" in dict:
    print("exist")
"""length of a dictionary"""
print(len(dict))
"""remove items and add"""
dict["v"]="vict"
print(dict)
dict.pop("name")
print(dict)
dict.popitem();
print(dict)
del dict["roll_no"]
print(dict)
dict.clear()
print(dict)
dict["name"] = "vuuu"
dict1 = dict.copy()
print(dict1)
dict.update({"name":"bunny"})
print(dict)
di.update({"name":"kittu"})
print(di)