class person:
    def name(self):
        print("the name is"+self.names)

p = person()
p.names = "kranthi"
p.name()

class phone:
    def __init__(self,name,ram,rom):
        self.name = name
        self.ram = ram
        self.rom = rom
    def pri(self,p):
        print(self.name,self.rom,self.ram)
        p.name()
pr = phone("honor",4,32)
pr.pri(p)

l = [x ** 2 for x in range(6,0,-1)]
print(l)
for i in range(7,1,-1):
    print(i)