# class Dog:
#      def _init_(self,breed):
#          self.breed = breed

# sam = Dog(breed='Lab')  # creating intsance for Dog class
# print(sam.breed)         

#-------------------------------------
# class Dog:
#     #class object attribute
#     species = 'mammels'

#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name

# sam = Dog('Lab','Sam')
# print(sam.species)   

#-------------------------------------------

# class Circle:
#     pi = 3.14

#     # by default provide value for radius=1
#     def __init__(self,radius=1):
#         self.radius = radius
#         self.area = radius * radius * Circle.pi

#     # reassign the radius
#     def setRadius(self,new_radius):
#         self.radius = new_radius
#         self.area = new_radius * new_radius * self.pi

#     # circumferenece
#     def getCircumference(self):
#         return self.radius * self.pi * 2

# a = Circle()
# print(a.radius) 
# print(a.area)
# print(a.getCircumference())

# a.setRadius(2)
# print('Radius is :',a.radius)
# print('Area is: ',a.area)
# print('Circumference is: ',a.getCircumference())   


#----------------------------------------------------------

# class Animal:
#     def _init_(self):
#         print('Animal created')

#     def whoAmI(self):
#         print('Animal')

#     def eat(self):
#         print('Eating')

# class Dog(Animal):
#     def _init_(self):
#         Animal._init_(self)
#         print('Dog created')

#     def whoAmI(self):
#         print('Dog')

#     def bark(self):
#         print('Woof')

# d = Dog()
# print(d.whoAmI())  
# print(d.eat())    


#--------------------------------------------------------------

# class Dog:
#     def _init_(self,name):
#         self.name = name
#     def speak(self):
#         return self.speak + 'says woof'

# class Cat:
#     def _init_(self,name):
#         self.name = name

#     def speak(self):
#         return self.name + 'says meow'

# # assign instance
# niko = Dog('Niko')
# felix = Cat('Felix')

# for pet in [niko,felix]:
#     print(pet.speak())
 
#-----------------------------------------------------------------------------

# class Circle:
#     pi = 3.14
#     def __init__(self,radius):
#         self.radius = radius
#         self.area = radius * radius * Circle.pi

#     def setRadius(self,new_radius):
#         self.radius = new_radius
#         self.area = new_radius * new_radius * self.pi

#     def setCircumference(self):
#         return self.radius * self.pi * 2

# c = Circle(3)
# c.setRadius(10)
# print(c.radius) 
# print(c.area)
# print(c.setCircumference())         

#------------------------------xxxxInheritancexxxxxxxxxxxx-----------------------
# class Animal:
#     def __init__(self):
#         print('Animal created')

#     def whoAmI(self):
#         print('Animal')

#     def eat(self):
#         print('Eating')

# class Dog(Animal):
#     def __init__(self):
#         print('Dog created')

#     def whoAmI(self):
#         print('Dog')

#     def bark(self):
#         print('barking')


# d = Dog()
# D = Animal()
# print(D.whoAmI())                                      

#----------------------------xxxxxpolymorphisamxxxxxxxxxxxxxx-------------------------------

# class Dog:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         return self.name + 'says woof!'

# class Cat:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         return self.name + 'says meow'

# c = Dog('Niko')
# d = Cat('Meko')
# print(c.speak())
# print(d.speak())  
# print(c.name)                      

#-----------------------------------------------------------------
# class Account:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance

#     def deposite(self,dep_amt):
#         self.balance += dep_amt
#         print('Deposite accepted')

#     def withdraw(self,wd_amt):
#         if self.balance>=wd_amt:
#             self.balance -= wd_amt
#             print('withdraw accepted')
#         else:
#             print('Fund unavailable')

#     def __str__(self):
#         return f'Account owner : {self.owner}\nAccount balance: {self.balance}'


# acc = Account('Jose',100)
# print(acc)
# print(acc.owner)
# print(acc.balance)    
# print(acc.withdraw)

# #--------
# -----------------------------------------------------------------

  


