# class Employee:
#     company = 'google'
     
#     def show_details(self):
#         print('this is reader')

# class Programmer(Employee):

#     def getlang(self):
#         print('This is a langugae')

#     def show_details(self):
#         print('this is me')

# c = Employee()
# d = Programmer()

# d.getlang()
# print(c.company)
# print(d.company)
# c.show_details()
# d.show_details()



#---------------multiinheritance----------------------------------

# class Employee:
#     company = 'Google'

# class Fiverr:
#     company = 'visa'
#     level = 0

#     def upgradelevel(self):
#         self.level = self.level + 1

# class Programmer(Fiverr,Employee):
#     name = 'say'

# p = Programmer()
# print(p.company)
# # p.upgradelevel() 
# print(p.level)      



#----------------super method--------------------------------------
# class Person:
#     country = 'India'

#     # def __init__(self):
#     #     print('Im working')

#     def takeBreath(self):
#         print("I am Breathing...")

# class Employee(Person):
#     Company = 'Honda'

#     # def __init__(self):
#     #     super().__init__()
#     #     print('Im reading')

#     def takeBreath(self):
#         super().takeBreath()
#         print('I am employe so i am breathing')

# class Programmer(Employee):
#     Company = 'Fiverr'

#     # def __init__(self):
#     #     super().__init__()
#     #     print('Im programmer')

#     def takeBreath(self):
#         super().takeBreath()
#         print('I am pragorammer so i am breathing')     

# # p = Person()
# # p.takeBreath()

# # e = Employee()
# # e.takeBreath ()

# pr = Programmer()
# pr.takeBreath()            


#-----------------class method-----------------------------------


# class Employee:
#     Company = 'Camel'
#     salary = 100             #class attribute            
#     Location = 'Pune'
    
#     # @classmethod
#     # def chnge_salry(cls,sal):
#     #      cls.salary = sal

# e = Employee()    
# # print(e.salary)
# # e.chnge_salry(41)
# # print(e.salary )
# Employee.salary = 54     #can use this method
# print(Employee.salary)
# print(e.salary )




#===================property decorator====================================== 
# class Employee:
#     company = 'gas'
#     salary = 5893
#     salarybonus = 153 

#     @property
#     def total_salary(self):
#         return self.salary + self.salarybonus

#     @total_salary.setter
#     def total_salary(self,totalsalary):
#         self.salarybonus = totalsalary - self.salary        

# e = Employee()
# print(e.total_salary)  
# e.total_salary = 56000
# print(e.salarybonus)   
# print(e.salary)




#-------------------operator overloading------------------------

# class Number:
#     def __init__(self,num):
#         self.num = num

#     def __add__(self,num2):
#         print('lets add numbers')
#         return self.num + num2.num

#     def __mul__(self,num2):
#         print('lets multiply numbers')
#         return self.num * num2.num   


# n1 = Number(4)
# n2 = Number(6)
# # sum = n1 + n2
# multiply = n1 * n2
# # print(sum)
# print(multiply)            


#----------------------------------
# class Number:
#     def __init__(self,num):
#         self.num = num

#     def __add__(self,num2):
#         print('lets add numbers')
#         return self.num + num2.num

#     def __str__(self):
#         return f"The number is :{self.num}"

#     def __len__(self):
#         return 1    #provide bydefault 1 lngth of numbers

# n = Number(9)
# print(n)  #here object is directly print so at that time use__str__()
# print(len(n))








