class computer:
    def __init__(self,ram,rom):
        self.ram = ram
        self.rom = rom
    def print(self):
        print(self.ram,self.rom)

class laptop(computer):
    def __init__(self,ram,rom,display,name):
        computer.__init__(self,ram,rom)
        self.display = display
        self.name = name
    def print(self):
        print(self.display,self.name,self.ram,self.rom)

lap = laptop(32,4,"dell",1080)
lap.print()
