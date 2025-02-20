class Car ():
    def __init__(self,name,wheels): 
        self.name = name
        self.wheels = wheels
    def drive(self):
        print(f"{self.name} is driving")
Toyota = Car("Toyota",4)
Merdeces = Car("Merdeces",4)
Toyota.drive()
Merdeces.drive()

