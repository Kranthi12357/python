class person:
    def __init__(self,name,kranthi):
        self.name = name
        self.kranthi = kranthi
    def func(self):
        print(self.kranthi,self.name)
person1 = person("kranthi",34)
print(person1.kranthi)
print(person1.name)
person1.func()