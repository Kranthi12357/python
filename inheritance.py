class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print(self):
        print(self.name,self.age)
def student(person):
    pass
p = person("kranthi",34)
p.print()