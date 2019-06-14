tuple = ("songs","audio","podcasts")
print(tuple)
#in tuple the elements are ordered and unchangeable
#and allow multiple elements
"""acessing the elements"""
print(tuple[1])
print(tuple[2])
"""we can't change the elements so no replace"""
"""traverse through tuple"""
for i in tuple:
    print(i)
"""check if exists"""
if "podcasts" in tuple:
    print("it exist")
"""to get length of a list"""
print(len(tuple))
"""count in tuple"""
print(tuple.count("podcasts"))
"""index of a element"""
print(tuple.index("podcasts"))
"""deleting completely"""
del tuple
print(tuple)