di = {
    "name":"kranthi",
    "age" : 30,
    "college":"cbit"
}
print(di)
print(di["name"])
print(di["college"])
di["age"] = 40
print(di)
del di["age"]
print(di)
di.update({"age":20})
print(di)
di.pop("age")
print(di)
di.popitem()
print(di)
for i,j in di.items():
    print(i,j)