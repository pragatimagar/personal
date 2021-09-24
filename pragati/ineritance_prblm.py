


#crete class 2d vector to create class 2d vector

# class C2dvec:
#     def __init__(self,i,j) :
#         self.i = i
#         self.j = j

#     def __str__(self):
#         return f"{self.i}i + {self.j}j"

# class C3dvec(C2dvec):
#     def __init__(self,i,j,k) :
#         super().__init__(i,j)
#         self.k = k

#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"   

# v2d = C2dvec(1,3)
# v3d = C3dvec(1,9,7)
# print(v2d)
# print(v3d)               


#-------------------------------------------------------------------------------------------------

# class Animal:
#     animaltype = "mammal"

# class Pet(Animal):
#     color = 'white'

# class Dog(Pet):
#     @staticmethod
#     def bark():
#         print('bow bow!')

# d = Dog()
# d.bark()                

#-------------------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-------------------------------
#salaryafterincrement = salary * increment

# class Employee:
#     salary = 1000
#     increment = 1.5
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary*self.increment

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,val):        #salaryafterincrement value is val
#         self.increment = val/self.salary

# e = Employee()
# print(e.salary)
# print(e.salaryAfterIncrement)   
# print(e.increment)  
# e.salaryAfterIncrement = 2000            #chnge salaryafterincrement to check increment
# print(e.increment)   



#--------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxx--------------------------------------
# class Complex:
#     def __init__(self,i,j):
#         self.real = i
#         self.imaginary = j

#     def __add__(self,c):
#         return Complex(self.real + c.real,self.imaginary + c.imaginary)  #doubt

#     def __mul__(self,c):
#         mulReal = self.real*c.real - self.imaginary*c.imaginary
#         mulImg = self.real*c.imaginary + self.imaginary*c.real
#         return Complex(mulReal,mulImg)  

#     def __str__(self):
#         return f"{self.real} + {self.imaginary}i"

# c1 = Complex(3,2)
# c2 = Complex(1,7) 
# print(c1+c2)
# print(c1*c2)



#---------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx----------------------------------

