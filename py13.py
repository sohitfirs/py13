# 1

class Transport:

   def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
       
   def a_print(self):
        print(f'Name transport: {self.name}, speed: {self.max_speed}, mileage: {self.mileage}')

abobus = Transport('Renaul Logan', 180, 12)

abobus.a_print()
print()

# 2

class Transport:

   def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
   def seating_capacity(self, capacity):
       return f'Capacity of one bus {self.name}: is {capacity} passengers'
   
class Authobus(Transport):
    
    seating_capacity_ = 50

    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
    
    def seating_capacity(self):
        return super().seating_capacity(self.seating_capacity_)    

bbb = Transport('Renaul Logan', 200, 100)
aaa = Authobus('Abobus', 100, 12)

print(bbb.seating_capacity(5))
print(aaa.seating_capacity())