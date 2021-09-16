class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        print('Employ is creaded')

    def GetDetails(self):
        print(f'the user is {self.name}')  

pragati = Employee('akshu',300)        
print(pragati.name)
pragati.GetDetails()